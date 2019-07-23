# relayserver
Bil452 Project

python create10mbfile.py -> 10mb dosya yaratır.

## Çalıştırılma Sırası
server -> relay -> client

## Progress
Step 1 bitti mi?
Step 3'ün bir kısmı bitti.

## TODO
- Step 2 -> func(p, bytestream) p = her byte'ın hatalı yollanma olasılığı, fonksiyon bytestream'i değiştirip print edecek.
- Step 3 -> Step 1'deki checksum yanlış geldiğinde tekrar gelecek şekilde düzelt. Rapor için p değerini 0'dan 10^-9'a kadar getir sonra daha da arttır. Belli bir eşik değerini aştığında hatasız gönderilme olasılığının 0'a yakınsadığını rapor et. p değeri için kaç kez tekrar gönderildiğini de rapor et.
- Step 4 -> p değeri belli bir değeri geçince yaşanan gecikmeler için RDT ilkelerini implement et. Bu değerleri 1 ve 3'teki kısımlarla karşılaştır.