# Agate evolver

__Instalacja potrzebnych bibliotek:__ pip install -r requirements.txt

## Agate evolver 2D

__Uruchomienie agate evolvera 2D:__ python3 draw.py

Agate evolver 2D umożliwia wygenerowanie agatu o narysowanym odręcznie obrysie. Pozwala na wgranie obrazu w formacie PNG, na którym można zaznaczyć kontur generowanego agatu. Wygenerowane obrazy można zapisać w formacie PNG.

Dostępne ustawienia:
*  `layer width`: Grubość kolejnych warstw generowanego agatu
*  `min area`: Gdy powierzchnia zamknięta przez wewnętrzne warstwy generowanego agatu spadnie poniżej tej wartości, generowanie jest przerywane

W folderze pictures znajdują się przykłady prawdziwych agatów oraz modeli wygenerowanych na podstawie ich konturów.

## Agate evolver 3D (przykład)

__Uruchomienie agate evolvera 3D:__ python3 3d_evolver_example.py

Przykład działania agate evolvera 3D generuje agat zaczynając od powierzchni będącej odkształconą sferą. Pozwala obserwować jego przekroje. Kółkiem myszy można przełączać się między warstwami.