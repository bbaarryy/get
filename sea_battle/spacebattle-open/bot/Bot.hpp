#ifndef BOT
#define BOT

#include "../engine/Field.hpp"
#include "../engine/Point.hpp"

// Interface for a Bot that is used in profilers. 
// To implement your own Bot, inherit from this class 
// and define all the virtual methods: destructor, 
// deployment and shooting.

class Bot {
public:
    virtual ~Bot() {};
    virtual void deploy(Field& field) = 0;
    virtual Point shoot(ShotResult previousShot) = 0;
};

#endif