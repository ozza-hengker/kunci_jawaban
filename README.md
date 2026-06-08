# 🚤 ROS2 & Gazebo Boat Simulation

Simulasi kapal otonom menggunakan **ROS 2 Humble** dan **Gazebo Sim**. Proyek ini mendemonstrasikan integrasi antara simulator fisik Gazebo dengan sistem robotika ROS2 untuk mengendalikan pergerakan kapal melalui topik `/cmd_vel`, baik secara **manual (teleoperation)** maupun **otonom**.

---

## 📖 Overview

Pada simulasi ini, sebuah kapal ditempatkan di dalam lingkungan kolam yang dibuat menggunakan Gazebo. Kapal dapat menerima perintah kecepatan linier dan angular dari ROS2 sehingga memungkinkan berbagai skenario pengendalian dan navigasi.

Fitur utama:

* 🌊 Simulasi lingkungan kolam air menggunakan Gazebo
* 🚤 Model kapal berbasis SDF
* 🎮 Kendali manual menggunakan keyboard
* 🤖 Kendali otonom berbasis ROS2 Node
* 🔄 Komunikasi real-time melalui topik `/cmd_vel`
* ⚡ Siap dikembangkan untuk navigasi, path planning, dan autonomous surface vehicle (ASV)

---

## 📂 Struktur Proyek

```text
ROS2-Gazebo-Boat-Simulation/
│
├── kolam.world          # Environment Gazebo
├── Kapal.sdf            # Model kapal dan plugin kontrol
├── kontrol.py           # Teleoperation menggunakan keyboard
├── kapal_otonom.py      # Kontrol otonom (Python)
├── kapal_otonom.cpp     # Kontrol otonom (C++)
└── README.md
```

### 📌 Deskripsi File

| File               | Deskripsi                                                                         |
| ------------------ | --------------------------------------------------------------------------------- |
| `kolam.world`      | Lingkungan simulasi Gazebo yang berisi kolam, pencahayaan, dan konfigurasi fisika |
| `Kapal.sdf`        | Model kapal beserta plugin kontrol kecepatan                                      |
| `kontrol.py`       | Node ROS2 untuk mengendalikan kapal menggunakan keyboard                          |
| `kapal_otonom.py`  | Implementasi kontrol otonom menggunakan Python                                    |
| `kapal_otonom.cpp` | Implementasi kontrol otonom menggunakan C++                                       |

---

## 🛠️ Requirements

Pastikan sistem telah terinstal:

* Ubuntu 22.04
* ROS2 Humble
* Gazebo Sim (Garden/Harmonic)
* Python 3
* Package ROS2:

  * `rclpy`
  * `geometry_msgs`
  * `std_msgs`

Cek instalasi ROS2:

```bash
source /opt/ros/humble/setup.bash
ros2 --version
```

---

## 🚀 Menjalankan Simulasi

### 1️⃣ Jalankan Environment Gazebo

```bash
gz sim kolam.world
```

---

### 2️⃣ Spawn Model Kapal

Jika kapal belum muncul otomatis:

```bash
gz service -s /world/default/create \
--reqtype gz.msgs.EntityFactory \
--reptype gz.msgs.Boolean \
--timeout 300 \
--req 'sdf_filename:"Kapal.sdf"'
```

---

### 3️⃣ Jalankan Bridge ROS2 ↔ Gazebo

```bash
ros2 run ros_gz_bridge parameter_bridge \
/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist
```

---

### 4️⃣ Kendali Manual

Jalankan node teleoperation:

```bash
python3 kontrol.py
```

Kontrol keyboard:

| Tombol | Aksi           |
| ------ | -------------- |
| W      | Maju           |
| S      | Mundur         |
| A      | Belok Kiri     |
| D      | Belok Kanan    |
| Q      | Keluar Program |

---

### 5️⃣ Jalankan Mode Otonom

Versi Python:

```bash
python3 kapal_otonom.py
```

Versi C++:

```bash
ros2 run nama_package kapal_otonom
```

---

## 📡 Topik ROS2

### Publisher

```text
/cmd_vel
```

Tipe pesan:

```text
geometry_msgs/msg/Twist
```

Contoh publish manual:

```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "
linear:
  x: 2.0
angular:
  z: 0.5"
```

---

## 🎯 Pengembangan Selanjutnya

Proyek ini dapat dikembangkan menjadi:

* Autonomous Surface Vehicle (ASV)
* Sistem waypoint navigation
* Path planning (A*, Dijkstra, RRT)
* Obstacle avoidance
* Integrasi GPS dan IMU virtual
* Multi-vehicle simulation
* Swarm surface robot

---

## 📸 Preview

Tambahkan screenshot atau GIF simulasi di sini.

```markdown
![Boat Simulation](images/demo.gif)
```

---

## 📚 Referensi

* ROS2 Documentation
* Gazebo Sim Documentation
* ros_gz_bridge

---

## 👨‍💻 Author

**Ozza**

Mahasiswa Teknik Komputer yang memilih membuat kapal virtual bergerak di kolam digital daripada menyentuh air sungguhan. Komputer memang lebih jarang bocor daripada kapal.
