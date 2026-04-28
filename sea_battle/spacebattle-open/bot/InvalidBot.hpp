#ifndef INVALIDBOT
#define INVALIDBOT

#include"Bot.hpp"
#include <iostream>

class InvalidBot : public Bot {
    static int counter;
public:
    virtual ~InvalidBot();
    virtual void deploy(Field& field) override;
    virtual Point shoot(ShotResult previousShot) override;
};

#endif
