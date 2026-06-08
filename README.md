# 🛥️ Autonomous Boat Simulation using ROS2 & Gazebo

Implementasi **Kapal Otonom (Autonomous Boat)** menggunakan **ROS2 Humble** dan **Gazebo Sim**. Pada studi kasus ini, kapal bergerak secara otomatis tanpa kendali keyboard dengan cara mengirimkan perintah kecepatan (`/cmd_vel`) secara berkala menggunakan **ROS2 Timer**.

---

## 🎯 Tujuan

Membuat sebuah node ROS2 yang dapat:

* Mengirim perintah kecepatan secara otomatis ke topik `/cmd_vel`
* Menggunakan mekanisme **Timer** untuk publish data secara terus-menerus
* Menggerakkan kapal tanpa bantuan teleoperation atau keyboard
* Menampilkan konsep dasar autonomous control pada simulasi Gazebo

---

## 📂 Struktur Proyek

```text
autonomous_boat/
│
├── kolam.world
├── Kapal.sdf
├── kapal_otonom.py
├── kapal_otonom.cpp
└── README.md
```

### Deskripsi File

| File               | Fungsi                                                     |
| ------------------ | ---------------------------------------------------------- |
| `kolam.world`      | Environment simulasi kolam pada Gazebo                     |
| `Kapal.sdf`        | Model kapal dan konfigurasi plugin kontrol                 |
| `kapal_otonom.py`  | Node ROS2 Python untuk mengendalikan kapal secara otomatis |
| `kapal_otonom.cpp` | Node ROS2 C++ untuk mengendalikan kapal secara otomatis    |

---

## 🛠️ Requirements

* Ubuntu 22.04
* ROS2 Humble
* Gazebo Sim
* Python 3 / C++
* Package ROS2:

  * `rclpy`
  * `geometry_msgs`
  * `rclcpp` (untuk C++)

---

## 🚀 Menjalankan Simulasi

### 1. Jalankan Gazebo

```bash
gz sim kolam.world
```

### 2. Jalankan Bridge ROS2 - Gazebo

```bash
ros2 run ros_gz_bridge parameter_bridge \
/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```

### 3. Jalankan Node Kapal Otonom

Versi Python:

```bash
python3 kapal_otonom.py
```

Versi C++:

```bash
ros2 run nama_package kapal_otonom
```

---

## ⚙️ Cara Kerja

Node akan membuat **Publisher** ke topik:

```text
/cmd_vel
```

Kemudian sebuah **Timer** akan memanggil fungsi callback secara berkala untuk mengirimkan pesan:

```text
geometry_msgs/msg/Twist
```

Dengan mengatur nilai:

```python
msg.linear.x
msg.angular.z
```

kapal dapat melakukan berbagai manuver seperti:

* Maju lurus
* Berputar di tempat
* Bergerak melingkar
* Zig-zag
* Pola navigasi sederhana lainnya

---

## 📌 Contoh Perilaku Kapal

Pada implementasi ini kapal bergerak membentuk lintasan melingkar dengan:

```python
msg.linear.x = 2.0
msg.angular.z = 0.5
```

Nilai kecepatan dapat dimodifikasi untuk menghasilkan pola gerakan yang berbeda.

---

## 📹 Hasil Simulasi

Video demonstrasi menunjukkan bahwa kapal dapat:

✅ Bergerak tanpa keyboard

✅ Menerima perintah otomatis dari node ROS2

✅ Bermanuver di dalam kolam Gazebo

---

## 👨‍💻 Author

**Ozza**

Studi kasus Integrasi ROS2 dan Gazebo untuk implementasi kapal otonom berbasis publish-subscribe architecture.
