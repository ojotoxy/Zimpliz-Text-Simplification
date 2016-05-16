# Zimpliz-Text-Simplification
An effortless English text simplification code, yet it surprisingly performs relatively better than other ready-to-use simplification softwares available.

Text simplification itu satu bahasan yang lumayan seru di bidang pemrosesan bahasa alami. Sesuai namanya, bahasan ini punya tujuan untuk menyederhanakan teks bacaan agar lebih gampang dipahami, tapi tentu tanpa mengubah atau mengurangi makna. Penyederhanaannya bisa dilakukan dari setidaknya dua cara: penyederhanaan secara leksikal (implementasinya biasanya dengan mengganti kata yang dianggap susah jadi kata lain yang lebih familiar) ataupun penyederhanaan struktur kalimat (sintaksis). Proyek ini fokus membahas metode penyederhanaan yang pertama.

Jadi, setelah dikompilasi, program Python ini bakal minta masukan berupa teks, be it as simple as a single word, a sentence or even some paragraphs. Keluarannya adalah teks yang (katanya sih) adalah versi yang lebih dapat dipahami daripada teks masukan. Lebih dapat dipahami, karena kata-kata yang susah (dalam proyek ini didefinisikan sebagai kata-kata yang jarang ditemui dalam tulisan sehari-hari) telah diganti dengan kata-kata yang lebih familiar karena kering digunakan.

## Example
Satu kalimat panjang yang diambil dari novel The Casual Vacancy oleh penulis legendaris J.K. Rowling
<pre>
input : Her face was a synthesis of perfect symmetry and unusual proportion; he could have gazed at it for hours, trying to locate the source of its fascination.
output : Her face was a synthesis of <b>complete balance</b> and <b>strange balance</b>; he could have <b>stare</b> at it for hours, trying to <b>place</b> the <b>beginning</b> of its fascination.
</pre>
