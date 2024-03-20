from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Inisialisasi koneksi ke MongoDB
client = MongoClient(os.getenv("MONGO_CONN"))
db = client.mydevDB
collection = db.users

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Definisi model Pydantic untuk permintaan
class UserRequest(BaseModel):
    username: str

# Definisi model Pydantic untuk permintaan membuat pengguna
class CreateUserRequest(BaseModel):
    nama: str
    username: str

# Fungsi untuk mencari pengguna berdasarkan nama pengguna
def find_user_by_username(username):
    result = collection.find_one({"username": username}, {"_id": 0, "nama": 1, "username": 1})
    
    # Jika pengguna tidak ditemukan, raise HTTPException dengan kode 404
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Jika pengguna ditemukan, kembalikan respons yang diinginkan
    return {"status": "200", "res": result}


# Endpoint untuk mencari pengguna berdasarkan nama pengguna
@app.get("/find")
def find_user(user_request: UserRequest):
    return find_user_by_username(user_request.username)

# Endpoint untuk membuat pengguna baru
@app.post("/create")
def create_user(user_request: CreateUserRequest):
    # Membuat dokumen pengguna baru berdasarkan permintaan
    new_user = {"nama": user_request.nama, "username": user_request.username}
    # Menyimpan dokumen pengguna baru ke MongoDB
    result = collection.insert_one(new_user)
    # Mengembalikan respons berhasil dengan ID dokumen baru
    return {"status": "201", "message": "User created successfully", "user_id": str(result.inserted_id)}

# Endpoint untuk menampilkan semua pengguna
@app.get("/users")
def show_all_users():
    # Mengambil semua dokumen pengguna dari MongoDB
    users = list(collection.find({}, {"_id": 0}))
    # Mengembalikan daftar pengguna
    return {"status": "200", "users": users}



# uvicorn main:app --reload --port 8001
