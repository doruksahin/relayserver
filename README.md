# relayserver
Bil452 Project

python create10mbfile.py -> 10mb dosya yaratır.

## Çalıştırılma Sırası
server -> relay -> client


## Progress
- Step 1 bitti. Fakat UDP'nin 10mb yollamasi 1-2 saniye kadar surerken TCP'nin yollanmasi 5dakika kadar suruyor, normal mi emin degilim.
- Step 2 bitti. 1024'luk veri icin 0'a yakinsayan hata degerini deneyerek bulmamiz gerekiyor, zor degil.
- Step 3 bitti. TCP kısmi test edilmedi.

## TODO
- Method aciklamalari iyilestirilecek.
- Paketlerin blocking yapmasi bizi bekletiyor. Paketler paralel gonderilebilir.

- Step 3 -> Rapor icin p degerini 0'dan 10^-9'a kadar getir sonra daha da arttir. Belli bir esik degerini astiginda hatasiz gonderilme olasiliginin 0'a yakinsadigini rapor et. p degeri icin kaç kez tekrar gonderildigini de rapor et.
- Step 4 -> p değeri belli bir degeri gecince yaşanan gecikmeler için RDT ilkelerini implement et. Bu değerleri 1 ve 3'teki kısımlarla karşılaştır.