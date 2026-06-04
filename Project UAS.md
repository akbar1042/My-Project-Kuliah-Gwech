Pada game ini (R.I.P Aim), pemain mengendalikan seorang pemanah
yang harus mengalahkan musuh pada setiap ronde. Setiap karakter memiliki kemampuan khusus yang berbeda 
sehingga permainan menjadi lebih bervariasi.

Game menerapkan konsep dunia side-scrolling dengan kamera yang mengikuti aksi, efek animasi, sistem save data, serta antarmuka seperti Main Menu, Shop, Pause Menu, Tutorial, dan Game Over Screen.

Untuk menjalankan nya harus menginstall modul pygame dan pillow terlebih dahulu agar dapat dijalankan di IDE yang digunakan

Fitur Utama:
1. Shop: Untuk membeli Character beserta meng-upgrade stats yang dimiliki oleh karakter
2. Play: Memulai permainan yang mana ketika musuh mati, maka round akan terus bertambah. Kemudian Stats dari musuh akan bertambah (Health dan Attack bertambah)
3. Skill: Setiap Character memiliki skill masing2 yang berbeda
4. Tutor: Tata cara bermain di sebelah kanan bawah pada Main Menu agar user dapat mengetahui cara bermain game nya

Implementasi OOP dalam projek:
1. Inheritance: Class Enemy dan Player merupakan turunan dari Class Character (Contoh: Class Player (Character))
2. Instance: Instance dari Class Enemy adalah variabel enemy dan instance dari Class Player adalah variabel player (Assignment variabel dengan Class yang dipakai)
3. Polymorphism: Class Enemy dan Player yang merupakan turunan dari Class Character merupakan salah satu penerapan Polymorphism yang mana method dari Class Enemy dan Class Player adalah berbeda (Contoh: Override: draw_arrow())
4. Enkapsulasi: Atribut yang dimiliki Class Enemy maupun Player tidak bisa diakses oleh Class lain karna bersifat private (Contoh: self.__health)

Nama Kelompok 4:
1. Tsaqif Fithrah Akbar (088)
2. Muaz Zulkarnain (087)
3. Ibrahem Jaudan (113)
4. Wildan Thoatullahh (244)
