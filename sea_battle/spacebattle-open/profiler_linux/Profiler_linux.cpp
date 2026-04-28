#include "Profiler_linux.hpp"
#include "../engine/TypesAndConsts.hpp"
#include "../engine/Engine.hpp"

#include "../bot/InvalidBot.hpp"
#include "../bot/MyBot.hpp"

#include <iostream>
#include <fstream>
#include <ncurses.h>
#include <array>
#define DEBUG false

using std::array;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::fstream;

void Profiler_linux::Log(Field& field)
{
    fstream file;
    file.open("Log.txt", std::ios::out | std::ios::app);
    for (int i = 0; i < FIELD_SIZE; i++)
    {
        for (int j = 0; j < FIELD_SIZE; j++)
        {
            file << field[i][j];
        }
        file << endl;
    }
    file << "\n\n";
    file.close();
}

void Profiler_linux::PrintField(const Field& field)
{
    initscr();
        
    start_color();
    init_pair(1, COLOR_BLUE, COLOR_BLACK);    // field
    init_pair(2, COLOR_BLACK, COLOR_WHITE);   // text 
    init_pair(3, COLOR_GREEN, COLOR_BLACK);   // ship
    init_pair(4, COLOR_MAGENTA, COLOR_BLACK); // hit
    init_pair(5, COLOR_CYAN, COLOR_BLACK);    // killed
    init_pair(6, COLOR_RED, COLOR_BLACK);     // miss
    attron(COLOR_PAIR(2));
        
    for (int i = 0; i < FIELD_SIZE; i++)
    {
        for (int j = 0; j < FIELD_SIZE; j++)
        {
            switch(field[i][j])
            {
                case 's':
                {   
                    attron(COLOR_PAIR(3)); 
                    printw("s ");
                    break;
                }
                case 'h':
                {
                    attron(COLOR_PAIR(4));
                    printw("x ");
                    break;
                }
                case 'm':
                {
                    attron(COLOR_PAIR(6));
                    printw("x ");
                    break;
                }
                case 'o':
                {   
                    attron(COLOR_PAIR(1));
                    printw("o ");
                    break;
                }
                case 'k':
                {   
                    attron(COLOR_PAIR(5));
                    printw("k ");
                    break;
                }
            }
        }
        printw("\n");
    }

    attron(COLOR_PAIR(2));
    mvaddstr(1, 40, "Press 'Space' to continue");
    attron(COLOR_PAIR(3));
    mvaddstr(3, 40, "s - alive ship");
    attron(COLOR_PAIR(4));
    mvaddstr(5, 40, "h - hitten ship");
    attron(COLOR_PAIR(6));
    mvaddstr(7, 40, "x - missed shoot");
    attron(COLOR_PAIR(1));
    mvaddstr(9, 40, "o - field");
    attron(COLOR_PAIR(5));
    mvaddstr(11, 40, "k - killed ship");
    getch();
    refresh();
    endwin();
}

void Profiler_linux::drop()
{
    move(0, 0);
}
