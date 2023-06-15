# Wtyczka do QGIS - PyQGIS
# Spis Treści:
- [Infomacje o programie](#informacje-o-programie)
- [Użycie wtyczki na przykładowych danych](#użycie-wtyczki-na-przykładowych-danych)
- [Znane błędy i niedoskonałości](#znane-błędy-i-niedoskonałości)

# Informacje o programie
Wtyczka oferuje następujące właściwości:
- obliczenie różnicy wysokości między dwoma punktami,
- obliczenie pole powierzchni na podstawie współrzędnych zaznaczonych punktów metodą Gaussa,
- aby skorzystać z wtyczki należy pobrać program QGIS w wersji 3.28.4 oraz wtyczke z zdalnego respozytorium,
- system operacyjny Windows 11.
- osbługuje dane o współrzędnych XYZ.
- obsługiwane formaty warstw z danymi wejściowymi to .shp (dla danych wektorowych) oraz .asc (dla rastrowych danych wysokościowych). Działanie dla innych formatów plików jest możliwe, jednakże nie zostało ono szeroko sprawdzone skąd takie próby są niezalecane.


# Użycie wtyczki na przykładowych danych 
Aby skorzystać z wtyczki należy pobrać i otworzyć program QGIS oraz wyszukać ją i zainstalowanie  w programie z sekcji 'wtyczki'.


![352822457_210796951873256_7899962594142674117_n](https://github.com/PlaceForNick/Projekt_2/assets/129080867/699c48db-0ed0-467f-92fe-e81721bddc88)

Przed wypróbowaniem wtyczki należy pobrać dane, które będą posiadać infomację o położeniu punktu (X,Y) oraz wysokości. Wybieramy naszą wtyczke z listy i wyświetla nam się panel roboczy wtyczki.

![353376590_1206222253412911_6168482014503073159_n](https://github.com/PlaceForNick/Projekt_2/assets/129080867/10b85030-76df-472b-9def-59925f98ccfd)



Wtyczka ma na celu w łatwy i przyjemny sposób liczyć różnicę wysokości oraz pola powierzchni poprzez zaznaczeniu przez użytkownika odpowiedniej ilości punktów. Dla obliczenia różnic wysokości musimy wskazać dwa punkty a dla pola minimum 3 punkty. Po zanzczeniu odpowiedniej ilości punktów wybieramy odpowiednią opcje i program powinnien nam pokazać wartości (dla różnicy wysokości w metrach a dla pola w metrach kwadratowych).

![349171127_5884694124969639_1341542513411203470_n](https://github.com/PlaceForNick/Projekt_2/assets/129080867/202328f5-434f-46e9-a1eb-223396a6b85f)
![352861351_213863917702505_4622197902513563315_n](https://github.com/PlaceForNick/Projekt_2/assets/129080867/57a76fee-6af6-4b22-8f36-3b62dc246de9)



# Znane błędy i niedoskonałości
## Format pliku
Próba uruchomienia wtyczki z użyciem niewspieranych typów plików może się nie powieść. Program nie jest w stanie obsłużyć wszstkich istniejących formatów plików, z oczywistych względów. W tym przypadku obsługiwane formaty to:
- .shp
- .asc

Przykładowe pliki o takich rozszerzeniach, na których były wykonywane testy zostały ujęte w repozytorium, pod folderm "przykladowe_warstwy". Aby je poprawnie wczytać należy zastosować układ współrzędnych EPSG:2180.
## Jednostki 
Na ten moment program drukuje nam wyniki w metrach i metrach kwadratowych, nie ma niestety możliwości wybrania w jakich jednostakch chce się uzykać wyniki operacji.
## Optymalizacja
Przy wyborze warstwy z ogromną ilością obiektów istnieje prawdopodobieństwo krótkiego zawieszenia programu.
## Obliczanie pola 
W szczególnych przypadkach algorytm wtyczki zaczyna obliczanie zgodnie z ruchem wskazówek zegara ,a następnie zmienia kierunek na przeciwny. Niestety na ten moment nie jesteśmy w stanie tego błędu poprawić.
## Obliczanie wysokości
W przypadku chęci obliczenia wysokości należy zwrócić uwagę aby warstwa wektorowa zawierająca punkty oraz warstwa rastrowa zawierająca NMT były w tym samym układnie współrzędnych. W przeciwnym razie program może uznać, iż punkty znajdują się poza warstwą podkładową i w konsekwencji zwrócić błąd.




