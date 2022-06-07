# rain-prediction-with-knn

## Deskripsi Singkat tentang Projek Ini

Sistem machine learning berbasis aplikasi web yang dapat melakukan prediksi akan turunnya hujan dan memberikan respon berdasarkan hasil prediksi tersebut. Responnya sendiri berupa simulasi penutupan atau pembukaan jendela atau kanopi atau alat pelindung hujan lainnya dalam web tersebut.

## Langkah-langkah yang Dapat Dilakukan Setelah Clone atau Download

1. Ketikkan command dibawah pada terminal PC atau Laptop Anda yang berada di path folder clone atau download

### Linux

sudo apt-get install python3-venv # If needed
python3 -m venv .venv
source .venv/bin/activate

### macOS

python3 -m venv .venv
source .venv/bin/activate

### Windows

py -3 -m venv .venv
.venv\scripts\activate

2. Buka folder clone atau download tersebut menggunakan Visual Studio Code (disarankan menggunakan Visual Studio Code)

3. Tekan Ctrl + Shift + P pada Visual Studio Code, ketikkan dan pilih option "Python: Select Interpreter"

4. Pilih versi python yang memiliki tulisan recommended di sampingnya atau yang memiliki path folder dengan tulisan "venv"

5. Ketikkan beberapa command dibawah pada terminal di Visual Studio Code

### python3 -m pip install --upgrade pip

### python3 -m pip install flask

### python3 -m pip install pandas

### python3 -m pip install seaborn

### python3 -m pip install openpyxl

### python3 -m pip install sklearn

6. Run aplikasi web dengan mengetikkan command di bawah ini pada terminal Visual Studio Code

### python -m flask run

7. Aplikasi web sudah dapat digunakan

## Cara Menggunakan Aplikasi Web

1. Masukkan input data berupa angka, bisa berupa desimal atau tidak, pada kolom-kolom yang telah disediakan

2. Bila semua kolom telah terisi, tekan tombol "Lakukan Prediksi" untuk memunculkan hasil prediksi dan juga respon sistem pada halaman web yang baru

3. Untuk kembali ke halaman awal, silahkan tekan kata-kata "Home" berwarna biru
