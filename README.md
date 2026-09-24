
# 🚀 **Inventory Management App – Flask**


<p align="center">
  <img src="assets/banner.png" alt="Inventory App Banner" />
</p>

---

## 📛 **Badges**

<p align="left">
  <img src="https://img.shields.io/badge/Framework-Flask-blue" />
  <img src="https://img.shields.io/badge/Frontend-TailwindCSS-38BDF8" />
  <img src="https://img.shields.io/badge/Database-SQLite-044a64" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen" />
  <img src="https://img.shields.io/badge/Author-Rumaisas--islam-pink" />
</p>

---

# ⭐ **Features**

✔️ User Registration & Login
✔️ Profile Page + Bio + Avatar
✔️ Add, Edit, Delete Items
✔️ Real-Time Search
✔️ Modern Dashboard with Analytics
✔️ Configurable low-stock alerts with item links
✔️ Clean UI/UX with Tailwind
✔️ Flash Messages for Feedback
✔️ Secure Password Hashing

---

# 📂 **Project Structure**

```
inventory_flask/
│── app.py
│── api.py
│── auth.py
│── config.py
│── dashboard.py
│── extensions.py
│── forms.py
│── inventory.db
│── LICENSE
│── main.py
│── models.py
│── profile.py
│── README.md
│── requirements.txt
│
├── assets/
│ └── banner.png
│
├── screenshots/
│ ├── add_item_1.png
│ ├── add_item_2.png
│ ├── change_password_1.png
│ ├── change_password_2.png
│ ├── dashboard_1.png
│ ├── dashboard_2.png
│ ├── edit_profile_1.png
│ ├── edit_profile_2.png
│ ├── home.png
│ ├── login.png
│ ├── profile.png
│ ├── register.png
│ ├── search.png
│ └── view.png
│
├── static/
│ ├── avatars/
│ ├── css/
│ └── uploads/
│
├── templates/
│ ├── 404.html
│ ├── 500.html
│ ├── add.html
│ ├── base.html
│ ├── change_password.html
│ ├── dashboard.html
│ ├── edit.html
│ ├── import_csv.html
│ ├── index.html
│ ├── login.html
│ ├── profile_edit.html
│ ├── profile.html
│ ├── register.html
│ ├── search.html
│ ├── view.html
│ └── ...
│
└── tests/
├── conftest.py
├── test_auth.py
├── test_models.py
└── test_routes.py
```

---

# 🛠️ **Tech Stack**

### **Backend**

* Flask
* Flask-Login
* Flask-WTF

### **Frontend**

* TailwindCSS
* Flowbite UI Components

### **Database**

* SQLite (default)
* SQLAlchemy ORM

### **Low-stock alerts**

The dashboard highlights each signed-in user's items whose quantity is below
`LOW_STOCK_THRESHOLD` (5 by default). The threshold can be adjusted in
`config.py`; alerts are sorted from the lowest quantity first and include a
direct link to each item. Items belonging to other users are never included.

---

# 🔧 **Installation Guide**

### **1️⃣ Clone Repo**

```bash
git clone https://github.com/KewaBrian/inventory-management-flask.git
cd inventory-management-flask
```

### **2️⃣ Create Virtual Environment**

```bash
python -m venv venv
```

### **3️⃣ Activate (Windows)**

```bash
venv\Scripts\activate
```

### **4️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **5️⃣ Run App**

```bash
flask run
```

---

# 📸 **Screenshots**

## 🏡 **Homepage**

<img src="screenshots/home.png" width="800"/>

---

## 📊 **Dashboard**

<img src="screenshots/dashboard_1.png" width="800"/>
<img src="screenshots/dashboard_2.png" width="800"/>

---

## ➕ **Add Item**

<img src="screenshots/add_item_1.png" width="800"/>
<img src="screenshots/add_item_2.png" width="800"/>

---

## 🔍 **Search Page**

<img src="screenshots/search.png" width="800"/>

---

## 👤 **Profile Page**

<img src="screenshots/profile.png" width="800"/>

---

## ✏️ **Edit Profile**

<img src="screenshots/edit_profile_1.png" width="800"/>
<img src="screenshots/edit_profile_2.png" width="800"/>

---

## 🔐 **Change Password**

<img src="screenshots/change_password_1.png" width="800"/>
<img src="screenshots/change_password_2.png" width="800"/>

---

## 🔑 **Login**

<img src="screenshots/login.png" width="800"/>

---

## 📝 **Register**

<img src="screenshots/register.png" width="800"/>

---

# 📄 **License**

This project is open-source and available under the **MIT License**.

---

