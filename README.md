# Project-data-types-python
This project about learning data types in python (In Indonesia)

Kita dapat memanggil atribut dtype untuk melihat tipe data masing - masing kolom pada dataframes tersebut. Dapat kita lihat bahwa kolom name, sex dan treatment a bertipe data object atau string sedangkan kolom treatment b disimpan dalam bentuk integer. Kolom numerik dapat berupa string atau sebaliknya, seperti yang terjadi untuk kolom treatment a. Kita dapat mengkonversi kolom ke string atau tipe object dengan menggunakan parameter di dalam method astype untuk kolom tersebut. 
Untuk variabel lain seperti kolom sex dapat kita ubah menjadi tipe data categories.
Dapat kita lihat sekarang jika tipe data sudah berubah di dalam dataframe tersebut.
Sekarang mari kita perhatikan kembali gambar “prepare and cleaning data”, dimana kolom treatment a disimpan dalam bentuk string karena ada nilai yang hilang (missing) ketika disimpan dengan simbol dash (-). Untuk kasus ini kita dapat menggunakan method to_numeric untuk kolom tersebut.
Disini kita juga gunakan parameter errors = ‘coerce’. Maka perintah ini akan mengkonversi semua nilai yang ada di kolom treatment a kedalam bentuk angka.
Untuk nilai yang invalid seperti simbol dash (-) sebelumnya, akan diberikan nilai default yaitu NaN missing value. Itulah gunanya parameter error = ‘coerce’. Jika kita tidak menggunakan parameter itu, maka Python akan menampilkan error. Karena Python tidak tahu cara mengubah string ke nilai numerik.
