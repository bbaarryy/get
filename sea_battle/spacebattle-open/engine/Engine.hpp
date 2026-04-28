#ifndef ENGINE
#define ENGINE

#include "Profiler.hpp"
#include "Field.hpp"
#include "Point.hpp"
#include "../bot/Bot.hpp"
#include <string>
#include <tuple>

using std::string;
using std::to_string;


class Engine {
private:
    Field field;
    int turn;                    // storing turns number for timeout

    bool ShipIsDead(Point shot);
    void setField(Field& src);

    Engine();
    std::tuple<bool, std::string> setFromDeploy(Bot& bot);
    ShotResult makeShot(Point shot);
    Field& getField();
public:
    static Engine& get_engine();

    bool checkField(string &err_mes); //checking of fleet deployment; /err_mes/ - is string for error output

    friend class Profiler;
};

#endif
