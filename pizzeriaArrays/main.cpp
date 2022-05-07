#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	//variabili
	int scelta = 0;
	float prezzoPizze[2];
	int rifare = 1;
	string nomePizze[2];
	
//ciclo while messo per decidere dopo se rifarlo o no il programma, manterra gli array salvati
while(rifare) {
	cout << "benvenuto, chi sei?\n1- ristoratore\n2- cliente\n";
	cin >> scelta;
	
	//switch fatto per decidere se ristoratore o cliente
	switch(scelta) {
		case 1:
			//2 cicli for per scrivere e 2 cicli for per leggere
			for (int i = 0; i < 2; i++ ) {
				cout << "scegliere il nome della pizza: ";
				cin >> nomePizze[i];
				cout << endl;

			}

			for (int i = 0; i < 2; i++ ) {
				cout << "scegliere il prezzo della pizza: ";
				cin >> prezzoPizze[i];
				cout << endl;
			}

			cout << "menu'\n";

			for (int i = 0; i < 2; i++) {
				cout << "nome: " << nomePizze[i] << " " << "prezzo: " << prezzoPizze[i] << " euro" << endl;
			}
			
			cout << "\n0- uscire\n1- continuare\n";
			cin >> rifare;	
			break;
			
		case 2:
			for (int i = 0; i < 2; i++) {
				cout << "nome: " << nomePizze[i] << " " << "prezzo: " << prezzoPizze[i] << " euro" << endl;
			}
			break;
			
		//default fatto per gli eventuali errori
		default:
			cout << "errore! hia selezionato un numero diverso da 0 e 1\n";
			rifare = 1;
	}
}	
	return 0;
}
