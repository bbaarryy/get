#include "Profiler.hpp"
#include "TypesAndConsts.hpp"
#include "Engine.hpp"

#include "../bot/InvalidBot.hpp"
#include "../bot/MyBot.hpp"

#include <iostream>
#include <fstream>
#include <array>
#include <ctime>

using std::array;
using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::fstream;

void Profiler::PrintResult(Result res)
{
    
}

void Profiler::drop() {}

Profiler::Result Profiler::PShootsB()
{
    Field field;

    Bot* player = new MyBot();
    Bot* bot = new InvalidBot();

    Engine& eng = Engine::get_engine();
    eng.setFromDeploy(*bot);
    ShotResult prevShot = FIRST_TURN;

    drop();
    PrintField(eng.getField());

    int turns = 0;

    Result result;

    auto clStart_round = clock();    
    while(prevShot != WIN and turns < FIELD_SIZE * FIELD_SIZE)
    {
        Point shot = player->shoot(prevShot);
        prevShot = eng.makeShot(shot);

        drop();
        PrintField(eng.getField());

        turns++;
        Log(eng.getField());
    }
    auto clEnd_round = clock();   
    
    result.round_ticks = clEnd_round - clStart_round;
    result.turns = turns;

    delete player;
    delete bot;
    return result;
}

Profiler::Result Profiler::BShootsP()
{
    int turns = 0;

    Field field;

    Bot* player = new MyBot();
    Bot* bot = new InvalidBot();
    
    Engine& eng = Engine::get_engine();
    auto res = eng.setFromDeploy(*player);

    Result result;

    if (!std::get<0>(res))
    {   
        cout << std::get<1>(res) << endl;
        result.turns = 0;
        result.round_ticks = 0;
    }
    else
    {
        ShotResult prevShot = FIRST_TURN;

        drop();
        PrintField(eng.getField());

        while(prevShot != WIN and turns <= FIELD_SIZE * FIELD_SIZE)
        {
            Point shot = bot->shoot(prevShot);
            prevShot = eng.makeShot(shot);

            drop(); 
            PrintField(eng.getField());

            turns ++;
            Log(eng.getField());
        }

        result.turns = turns;
    }

    delete player;
    delete bot;
    return result;
}

Profiler::Result Profiler::PShootsP()
{
    int turns = 0;

    Field field;

    Bot* player = new MyBot();
    
    Engine& eng = Engine::get_engine();
    auto res = eng.setFromDeploy(*player);
    Result result;

    if (!std::get<0>(res))
    {   
        cout << std::get<1>(res) << endl;
        result.turns = 0;
        result.round_ticks = 0;
    }
    else
    {    
        ShotResult prevShot = FIRST_TURN;

        drop();
        PrintField(eng.getField());

        while(prevShot != WIN and turns <= FIELD_SIZE * FIELD_SIZE)
        {
            Point shot = player->shoot(prevShot);
            prevShot = eng.makeShot(shot);
            
            drop();
            PrintField(eng.getField());

            turns ++;
            Log(eng.getField());
        }

        result.turns = turns;
    }

    delete player;
    return result;
}


Profiler::Result Profiler::BShootsB()
{
    Field field;

    Bot* bot = new InvalidBot();

    Engine& eng = Engine::get_engine();
    eng.setFromDeploy(*bot);
    ShotResult prevShot = FIRST_TURN;

    drop();
    PrintField(eng.getField());

    int turns = 0;

    while(prevShot != WIN and turns <= FIELD_SIZE * FIELD_SIZE)
    {
        Point shot = bot->shoot(prevShot);
        prevShot = eng.makeShot(shot);

        drop();
        PrintField(eng.getField());

        turns ++;
        Log(eng.getField());
    }


    Result result;
    result.turns = turns;

    delete bot;
    return result;
}

Profiler::Result Profiler::SwitchModes()
{
    int mode;
    cout << "\nEnter mode number: " << endl;
    cout << "// Enter 0 for list of modes //\n" << endl;
    cin >> mode;
    switch (mode)
    {
        case 0:
        {
            cout << "1 - Your bot shoots down invalidbot's field" << endl;
            cout << "2 - Invalidbot shoots down your field" << endl;
            cout << "3 - Your bot shoots down your field" << endl;
            return SwitchModes();
        }
        case 1:
        {
            return PShootsB();
        }
        case 2:
        {
            return BShootsP();
        }
        case 3:
        {
            return PShootsP();
        }
        default:
        {
            cout << "Wrong mode" << endl;
            Result result;
            result.round_ticks = 0;
            result.turns = 0;
            return result;
        }
    }
}

