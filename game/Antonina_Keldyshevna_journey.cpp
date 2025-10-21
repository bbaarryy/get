// #pragma GCC optimize "O1"

#include <iostream>
#include <fstream>
#include <thread>
#include <random>

using std::cout, std::endl, std::this_thread::sleep_for;
using namespace std::chrono_literals;
std::ofstream logfile;
									            //		      YOU CAN SET THESE CONSTS WHILE DEBUGING
const int TIME_TO_SLEEP = 250;					//  <======== Animation delay (ms)
const bool PRINT_STEPS = true;					//  <======== Enable / disable animation
const int STEPS_LIMIT =  256;					//  <======== Steps limit for each run
const int N_TESTS = 10;						    //  <======== Number of each test runs (>=100 for statistics)

//	=========================================  YOUR CODE HERE  ==========================================
//	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|
//	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v
bool first_step = 1;
bool obhod = 0;
bool go_to = 1;
                            //  <======== Your global values.
bool go_home = 1;

bool chnge = 1;
std::string obh_s = "!";
int end_steps=0;
int ind = 0;
int ind2 = 0;
bool rr = 1;
std::string path ="";

bool if1 = 1;
bool if2 = 1;
bool if3 = 1;
bool if4 = 1;

void Reset()                                    //  <======== You can set or reset you globals
{             
	end_steps=0;
	path = ""; 
	obh_s = "!";	                              	//            before each test.
	first_step = 1;
	obhod=0;
	ind=0;
	rr=1;
	logfile << "clear" << endl; 
}

// void MyOwnFunc(){}                           //  <======== You can add you functions here.

char horiz_move(char map[][8], int ant_x, int ant_y, int home_x, int home_y, int sample_x, int sample_y){
	if(first_step){
		if(sample_y < home_y){
			first_step = 0;
			return('r');
		}
		else if(sample_y > home_y){
			first_step = 0;
			return('l');
		}
	}
	else{
		if(obhod == 0){
			if(obh_s=="!"){
				if(ant_x > 0){
					if(sample_y < home_y){
						obh_s = "ulld";
					}
					else{
						obh_s = "urrd";
					}
				}
				else{
					if(sample_y < home_y){
						obh_s = "dllu";
					}
					else{
						obh_s = "drru";
					}
				}
			}
			ind++;
			if(ind-1 == 3){obhod=1;}
			return(obh_s[ind-1]);
		}
		else{
			if(sample_y > home_y){
				return('l');
			}
			else{
				return('r');
			}
		}
	}

	return ('q');
}

char Move(char map[][8], int ant_x, int ant_y, int home_x, int home_y, int sample_x, int sample_y) // <======= YEP, THIS IS IT
{
	//without rocks
	if((home_x == sample_x && ant_x == home_x) || (ant_y == home_y && home_y == sample_y) || end_steps){
		if(sample_x == home_x){
			if(ant_y < sample_y-1){return 'r';}
			else if(ant_y > sample_y+1){return 'l';}
			else{
				end_steps=1;
				char t = horiz_move(map,ant_x,ant_y,home_x,home_y,sample_x,sample_y);return t;}
		}
		else if(sample_y == home_y){
			if(ant_x < sample_x-1){return 'd';}
			else if(ant_x > sample_x+1){return 'u';}
			else{
				end_steps=1;
				char t = horiz_move(map,ant_y,ant_x,home_y,home_x,sample_y,sample_x);
				if(t=='u')return('r');
				if(t=='d')return('l');
				if(t=='l')return('u');
				if(t=='r')return('d');
			}
		}
	}

	else{
		//идём до горизонтали
		if(path == ""){
		while(ant_x != sample_x){
			if(ant_x > sample_x){
				path+='u';
				ant_x--;
			}
			else if(ant_x < sample_x){
				path +='d';
				ant_x++;
			}
		}

		while(sample_y != home_y){
			if(ant_y < sample_y-1){
				path += 'r';
				ant_y ++;
			}
			else if(ant_y > sample_y+1){
				path += 'l';
				ant_y--;
			}
			else{
				while(sample_y != home_y){
					char t = horiz_move(map,ant_x,ant_y,home_x,home_y,sample_x,sample_y);
					path+=t;
					if(t == 'r'){
						if((sample_y == ant_y+1 || sample_y==ant_y-1) && sample_x == ant_x){sample_y++;}
						ant_y++;}
					if(t == 'l'){
						if((sample_y == ant_y-1 || sample_y == ant_y+1) && sample_x == ant_x){sample_y--;}
						ant_y--;}
					if(t == 'u'){ant_x--;}
					if(t == 'd'){ant_x++;}
				}
			}
		}

		if(ant_x == sample_x){
			if(ant_x > home_x){
				path += 'u';
				ant_x--;
			}
			else{path+='d';ant_x++;}
		}
		if(ant_y != sample_y){
			if(ant_y > home_y){
				path+='l';ant_y--;
			}
			else{path+='r';ant_y++;
			}
		}
		ind2=1;
		ind=0;
		first_step=1;
		obhod = 0;
		obh_s = "!";
		return path[0];
		}
		else if(ind2 <= path.size()){
			ind2++;
			
			return path[ind2-1];
		}
	}
	return('e');
}

//	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^	^
//	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|
//	=========================================  YOUR CODE HERE  ==========================================



//	========================================= ! DO NOT TOUCH ! ==========================================
//	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|	|
//	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v	v

void ClearLab(char lab[][8])
{
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			lab[i][j] = '.';
}
void PrintLab(char lab[][8])
{
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++)
			printf("%c ", lab[i][j]); // cout << lab[i][j] << ' ';
		printf("\n");// cout << endl;
	}
}
bool MakeLab(char lab[][8], int ax, int ay, int Ox, int Oy, int gx, int gy, int rn, int rx[], int ry[])
{
	ClearLab(lab);
	if ((gx == ax && gy == ay) || (gx == Ox && gy == Oy)) { return false; }

	for (int i=0;i<rn;i++)
		lab[rx[i]][ry[i]] = '#';
	if (ax == Ox && ay == Oy)
		lab[ax][ay] = '@';
	else
	{
		lab[ax][ay] = 'a';
		lab[Ox][Oy] = 'O';
	}
	lab[gx][gy] = '%';
	return true;
}
void CopyLab(char lab[][8], char copy[][8], int* ax, int* ay, int* Ox, int* Oy, int* gx, int* gy)
{
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
		{
			copy[i][j] = lab[i][j];
			switch (copy[i][j])
			{
			case 'a': *ax = i; *ay = j; break;
			case '%': *gx = i; *gy = j;	break;
			case 'O': *Ox = i; *Oy = j;	break;
			case '@': *ax = i; *ay = j; *Ox = i; *Oy = j; break;
			default: break;
			}
		}
}

bool MakeLab(char lab[][8], int ax, int ay, int Ox, int Oy, int gx, int gy, int rn)
{
	int rx[64] = { 0 };
	int ry[64] = { 0 };

	if (!MakeLab(lab, ax, ay, Ox, Oy, gx, gy, 0, rx, ry))
    {
        logfile<<"GEN-ERR";
        return false;
    }


	int count = rn;
	int stop = 16;
	while (count > 0) {
		for (int i = 0; i < 8; i++)
			for (int j = 0; j < 8; j++)
			{
				if (lab[i][j] == '.' && rand() % 64 < rn && (abs(i - Ox) + abs(j - Oy) > 2))
				{
					lab[i][j] = '#'; count--;
					if (count == 0) return true;
				}
			}
		stop--;
		if (stop == 0)return false;
	}
	return true;
}

int GoTest(char lab[][8], bool doprint)
{
    logfile<<"#\tNew test... ";
	Reset();
	for (int s = 1; s < STEPS_LIMIT+1; s++)
	{
		if (doprint)
		{
			sleep_for(std::chrono::milliseconds(TIME_TO_SLEEP));
			//system("CLS");
			printf("Step: %d / %d                       \n",s, STEPS_LIMIT);
			PrintLab(lab);
			for (int l = 0; l < 9; l++)
			{
				printf("\r\033[A");
			}
		}
		char copy[8][8];
		int ax, ay, Ox, Oy, gx, gy;
		CopyLab(lab, copy, &ax, &ay, &Ox, &Oy, &gx, &gy);
		char c = Move(copy, ax, ay, Ox, Oy, gx, gy);
		if (c=='x') {logfile<<" terminated at step "<<s<<"!\n"; return -1;} //breaking this ant run
		if (c=='q') {logfile<<" terminated!\n"; return -2;} //breaking this ant run

		int tox = ax, toy = ay, totox = ax, totoy = ay, pullx = ax, pully = ay;
		bool toB = true, totoB = true, pullB = true;
		switch (c)
		{
		case 'u': tox--; totox -= 2; pullx++; toB = (tox >= 0); totoB = (totox >= 0); pullB = (pullx < 8); break;
		case 'd': tox++; totox += 2; pullx--; toB = (tox < 8); totoB = (totox < 8); pullB = (pullx >= 0); break;
		case 'l': toy--; totoy -= 2; pully++; toB = (toy >= 0); totoB = (totoy >= 0); pullB = (pully < 8); break;
		case 'r': toy++; totoy += 2; pully--; toB = (toy < 8); totoB = (totoy < 8); pullB = (pully >= 0); break;
		default: //FAIL
			break;
		}
		if (!toB) continue; //wall
		if (lab[tox][toy] == '.' || lab[tox][toy] == 'O') //simple move or pull
		{
			lab[tox][toy] = (lab[tox][toy] == '.') ? 'a' : '@';
			if (!pullB || lab[pullx][pully] == '.' || lab[pullx][pully] == 'O') { lab[ax][ay] = (lab[ax][ay] == 'a') ? '.' : 'O'; continue; }//simple move
			if (lab[pullx][pully] == '%' && lab[ax][ay] == '@') { logfile<<" done in "<<s<<" steps!\n"; return s; }//DONE with pull
			if (lab[pullx][pully] == '#' && lab[ax][ay] == '@') { lab[ax][ay] = 'O';  continue; } //cant pull # to O
			lab[ax][ay] = lab[pullx][pully]; lab[pullx][pully] = '.'; continue;//pull # or %

		}
		if (lab[tox][toy] == '%')
		{
			if (!totoB || lab[totox][totoy] == '#') continue; //wall or blocked
			if (lab[totox][totoy] == '.') { lab[tox][toy] = 'a'; lab[ax][ay] = (lab[ax][ay] == 'a') ? '.' : 'O'; lab[totox][totoy] = '%'; continue; } //push % to .
			if (lab[totox][totoy] == 'O') { logfile<<" done in "<<s<<" steps!\n"; return s; } //DONE with push
		}
		if (lab[tox][toy] == '#')
		{
			if (!totoB || lab[totox][totoy] != '.') continue; //wall or blocked
			lab[tox][toy] = 'a'; lab[ax][ay] = (lab[ax][ay] == 'a') ? '.' : 'O';; lab[totox][totoy] = '#'; continue;  //push # to .
		}
	}
	logfile<<" fail!\n";
	return -1;
}

void StopAll()
{
    cout << "Terminated!" << endl;
	logfile << "#####\tTerminated!\n";
    logfile.close();
    exit(0);
}

int main()
{
    printf("Starting new Antonina runs!\nSTEPS_LIMIT=%d N_TESTS=%d\n",STEPS_LIMIT,N_TESTS);
    logfile.open ("antlog.txt");
    logfile << "#####\tStarting new Antonina runs!\n#####\tSTEPS_LIMIT="<<STEPS_LIMIT<<"\tN_TESTS="<<N_TESTS<<"\n";
	srand(time(NULL));
	char lab[8][8];
	int rx[64];
	int ry[64];
	int nr = 0;
	int wins;
	int sum;
	int score,wr,as;
	int totalscore = 0;

	// //Test 00 	one line not at walls
	// logfile << "#####\tStarting Test 00...\n";
	// wins = 0; sum = 0;
	// for (int i = 0; i < N_TESTS; i++)
	// {
	// 	int ax = 1 + rand() % 6, ay = 1 + rand() % 6;
	// 	int gx = ax, gy = ay;
	// 	if (rand() % 2 == 0) while (gx == ax) gx = 1 + rand() % 6;
	// 	else while (gy == ay) gy = 1 + rand() % 6;
	// 	MakeLab(lab, ax, ay, ax, ay, gx, gy, 0);
	// 	//test
	// 	printf("Test 00: %d/%d             \n",i,N_TESTS);
	// 	int res = GoTest(lab, PRINT_STEPS);
	// 	if (res > 0) { wins++; sum += res; }
	// 	else if(res==-2) StopAll();
	// 	printf("\r\033[A");
	// }
	// score = 100*(wins * STEPS_LIMIT - sum)/ STEPS_LIMIT/ N_TESTS;
	// totalscore += score;
	// wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	// printf("Test 00: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	// logfile << "#####\tTest 00: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	// //Test 01 	no line not at walls
	// logfile << "#####\tStarting Test 01...\n";
	// wins = 0; sum = 0;
	// for (int i = 0; i < N_TESTS; i++)
	// {
	// 	int ax = 1 + rand() % 6, ay = 1 + rand() % 6;
	// 	int gx = ax, gy = ay;
	// 	while (gx == ax) gx = 1 + rand() % 6;
	// 	while (gy == ay) gy = 1 + rand() % 6;
	// 	MakeLab(lab, ax, ay, ax, ay, gx, gy, 0);
	// 	//test
	// 	printf("Test 01: %d/%d             \n", i, N_TESTS);
	// 	int res = GoTest(lab, PRINT_STEPS);
	// 	if (res > 0) { wins++; sum += res; }
	// 	else if(res==-2) StopAll();
	// 	printf("\r\033[A");
	// }
	// score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	// totalscore += score;
	// wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	// printf("Test 01: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	// logfile << "#####\tTest 01: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	// //Test 02 	one line O at wall
	// logfile << "#####\tStarting Test 02...\n";
	// wins = 0; sum = 0;
	// for (int i = 0; i < N_TESTS; i++)
	// {
	// 	int ax = 1 + rand() % 6, ay = 1 + rand() % 6;
	// 	if (rand() % 2 == 0) ax = (rand() % 2 == 0) ? 0 : 7;
	// 	else ay = (rand() % 2 == 0) ? 0 : 7;
	// 	int gx = ax, gy = ay;
	// 	if (rand() % 2 == 0) while (gx == ax) gx = rand() % 8;
	// 	else while (gy == ay) gy = rand() % 8;
	// 	MakeLab(lab, ax, ay, ax, ay, gx, gy, 0);
	// 	//test
	// 	printf("Test 02: %d/%d             \n", i, N_TESTS);
	// 	int res = GoTest(lab, PRINT_STEPS);
	// 	if (res > 0) { wins++; sum += res; }
	// 	else if(res==-2) StopAll();
	// 	printf("\r\033[A");
	// }
	// score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	// totalscore += score;
	// wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	// printf("Test 02: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	// logfile << "#####\tTest 02: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 03 	all in corners
	logfile << "#####\tStarting Test 03...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax = (rand() % 2 == 0)?0:7, ay = (rand() % 2 == 0) ? 0 : 7;
		int gx = ax, gy = ay;
		while (gx == ax && gy == ay)
		{
			gx = (rand() % 2 == 0) ? 0 : 7;
			gy = (rand() % 2 == 0) ? 0 : 7;
		}
		MakeLab(lab, ax, ay, ax, ay, gx, gy, 0);
		//test
		printf("Test 03: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 03: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 03: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 04 	at 1 line with 1 #
	logfile << "#####\tStarting Test 04...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax = rand() % 8, ay = rand() % 8;
		int gx = ax, gy = ay;
		if (rand() % 2 == 0) while (abs(gx - ax) < 2) gx = rand() % 8;
		else while (abs(gy - ay) < 2) gy = rand() % 8;
		rx[0] = (gx + ax) / 2;
		ry[0] = (gy + ay) / 2;
		MakeLab(lab, ax, ay, ax, ay, gx, gy, 1, rx, ry);
		//test
		printf("Test 04: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 04: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 04: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 05 	not at 1 line with 2 #
	logfile << "#####\tStarting Test 05...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax = rand() % 8, ay = rand() % 8;
		int gx = ax, gy = ay;
		while (gx == ax) gx = rand() % 8;
		while (gy == ay) gy = rand() % 8;
		rx[0] = gx;	ry[0] = ay;
		rx[1] = ax;	ry[1] = gy;
		MakeLab(lab, ax, ay, ax, ay, gx, gy, 2, rx, ry);
		//test
		printf("Test 05: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 05: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 05: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Tests 06-09 	not at 1 line with many #
	nr = 4;
	for (int k = 0; k < 4; k++)
	{
        logfile << "#####\tStarting Test 0"<<k+6<<"...\n";
		wins = 0;
		sum = 0;
		for (int i = 0; i < N_TESTS; i++)
		{
			int ax = rand() % 8, ay = rand() % 8;
			int gx = ax, gy = ay;
			while (gx == ax) gx = rand() % 8;
			while (gy == ay) gy = rand() % 8;
            bool done = false;
            while(!done)
			    done = MakeLab(lab, ax, ay, ax, ay, gx, gy, nr);
			//test
			printf("Test 0%d: %d/%d             \n", 6+k, i, N_TESTS);
			int res = GoTest(lab, PRINT_STEPS);
			if (res > 0) { wins++; sum += res; }
			else if(res==-2) StopAll();
			printf("\r\033[A");
		}
		score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
		totalscore += score;
		wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
        printf("Test 0%d: winrate=%d%% av.steps=%d score=%d\n",6+k, wr, as, score);
        logfile << "#####\tTest 0"<<k+6<<": winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";
		nr *= 2;
	}

	//Test 10 1 block line
	logfile << "#####\tStarting Test 10...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax, ay, gx, gy;
		nr = 8;
		if(rand() % 2 == 0) //vert
		{
			ax = rand() % 8; gx = rand() % 8;
			if (rand() % 2 == 0) {ay = rand() % 2; gy = 6+rand() % 2;}
			else {ay = 6 + rand() % 2; gy = rand() % 2;}
			int y = 2 + rand() % 4;
			for (int ir = 0; ir < 8; ir++) { rx[ir] = ir; ry[ir] = y; }
		}
		else
		{
			ay = rand() % 8; gy = rand() % 8;
			if (rand() % 2 == 0) {ax = rand() % 2; gx = 6 + rand() % 2;}
			else {ax = 6 + rand() % 2; gx = rand() % 2;}
			int x = 2 + rand() % 4;
			for (int ir = 0; ir < 8; ir++) { rx[ir] = x; ry[ir] = ir; }
		}
		MakeLab(lab, ax, ay, ax, ay, gx, gy, nr, rx, ry);
		//test
		printf("Test 10: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 10: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 10: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 11 2 block lines
	logfile << "#####\tStarting Test 11...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax, ay, gx, gy;
		nr = 16;
		if (rand() % 2 == 0) //vert
		{
			ax = rand() % 8; gx = rand() % 8;
			if (rand() % 2 == 0) { ay = rand() % 2; gy = 6 + rand() % 2; }
			else { ay = 6 + rand() % 2; gy = rand() % 2; }
			int y= 2 + rand() % 3;
			for (int ir = 0; ir < 8; ir++) { rx[ir * 2] = ir; ry[ir * 2] = y; rx[ir * 2 + 1] = ir; ry[ir * 2 + 1] = y + 1; }
		}
		else
		{
			ay = rand() % 8; gy = rand() % 8;
			if (rand() % 2 == 0) { ax = rand() % 2; gx = 6 + rand() % 2; }
			else { ax = 6 + rand() % 2; gx = rand() % 2; }
			int x = 2 + rand() % 3;
			for (int ir = 0; ir < 8; ir++) { rx[ir * 2] = x; ry[ir * 2] = ir; rx[ir * 2 + 1] = x+1; ry[ir * 2 + 1] = ir; }
		}
		MakeLab(lab, ax, ay, ax, ay, gx, gy, nr, rx, ry);
		//test
		printf("Test 11: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 11: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 11: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 12 3 block lines
    logfile << "#####\tStarting Test 12...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax, ay, gx, gy;
		nr = 24;
		if (rand() % 2 == 0) //vert
		{
			ax = rand() % 8; gx = rand() % 8;
			if (rand() % 2 == 0) { ay = rand() % 2; gy = 6 + rand() % 2; }
			else { ay = 6 + rand() % 2; gy = rand() % 2; }
			int x = 2 + rand() % 2;
			for (int ir = 0; ir < 8; ir++)
				for (int ik = 0; ik < 3; ik++) { rx[ir * 3 + ik] = ir; ry[ir * 3 + ik] = x+ik; }
		}
		else
		{
			ay = rand() % 8; gy = rand() % 8;
			if (rand() % 2 == 0) { ax = rand() % 2; gx = 6 + rand() % 2; }
			else { ax = 6 + rand() % 2; gx = rand() % 2; }
			int y = 2 + rand() % 2;
			for (int ir = 0; ir < 8; ir++)
				for (int ik = 0; ik < 3; ik++) { rx[ir * 3 + ik] = y + ik; ry[ir * 3 + ik] = ir; }
		}
		MakeLab(lab, ax, ay, ax, ay, gx, gy, nr, rx, ry);
		//test
		printf("Test 12: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 12: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 12: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//Test 13 4 block lines
	logfile << "#####\tStarting Test 13...\n";
	wins = 0; sum = 0;
	for (int i = 0; i < N_TESTS; i++)
	{
		int ax, ay, gx, gy;
		nr = 32;
		if (rand() % 2 == 0) //vert
		{
			ax = rand() % 8; gx = rand() % 8;
			if (rand() % 2 == 0) { ay = rand() % 2; gy = 6 + rand() % 2; }
			else { ay = 6 + rand() % 2; gy = rand() % 2; }
			for (int ir = 0; ir < 8; ir++)
				for (int ik = 0; ik < 4; ik++) { rx[ir * 4 + ik] = ir; ry[ir * 4 + ik] = 2+ik; }
		}
		else
		{
			ay = rand() % 8; gy = rand() % 8;
			if (rand() % 2 == 0) { ax = rand() % 2; gx = 6 + rand() % 2; }
			else { ax = 6 + rand() % 2; gx = rand() % 2; }
			for (int ir = 0; ir < 8; ir++)
				for (int ik = 0; ik < 4; ik++) { rx[ir * 4 + ik] = 2 + ik; ry[ir * 4 + ik] = ir; }
		}
		MakeLab(lab, ax, ay, ax, ay, gx, gy, nr, rx, ry);
		//test
		printf("Test 13: %d/%d             \n", i, N_TESTS);
		int res = GoTest(lab, PRINT_STEPS);
		if (res > 0) { wins++; sum += res; }
		else if(res==-2) StopAll();
		printf("\r\033[A");
	}
	score = 100 * (wins * STEPS_LIMIT - sum) / STEPS_LIMIT / N_TESTS;
	totalscore += score;
	wr = 100 * wins / N_TESTS; as = wins > 0 ? sum / wins : 0;
	printf("Test 13: winrate=%d%% av.steps=%d score=%d\n", wr, as, score);
	logfile << "#####\tTest 13: winrate="<<wr<<"% av.steps=" << as<<" score="<<score<<"\n";

	//end
	cout << "Total score = " << totalscore << endl;
	logfile << "#####\tAll done!\n";
        logfile.close();
	return 0;
}