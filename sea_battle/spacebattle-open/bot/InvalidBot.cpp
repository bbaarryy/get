#include "InvalidBot.hpp"

int InvalidBot::counter = -1;

InvalidBot::~InvalidBot() {}

Point InvalidBot::shoot(ShotResult previousShot) {
    switch (previousShot) {
        case WIN:
            return Point{0, 0};
        default:
            counter++;
            if (counter > 168)
                return Point{0, 0};
            if (counter == 0) {
                return Point{0, 0};
            } else {
                return Point{counter % FIELD_SIZE, counter / FIELD_SIZE};
            }
    }
}

void InvalidBot::deploy(Field& field) {
    for(size_t i = 0; i<FIELD_SIZE; i++){
        for(size_t j = 0; j<FIELD_SIZE; j++){
            field[i][j] = 'o';
        }
    }
    Point coord{FIELD_SIZE - 1, 0};
    for (std::size_t i = 0; i < 3; i++) { //set 3 x 2 ships
        for (std::size_t j = 0; j < 2; j++) {
            field[coord.get_y()][coord.get_x()] = 's';
            coord.inc_y();
        }
        coord.inc_y();
    }

    coord = {FIELD_SIZE - 1, FIELD_SIZE - 1};
    for (std::size_t i = 0; i < 2; i++) { //set 2 x 3 ships
        for (std::size_t j = 0; j < 3; j++) {
            field[coord.get_y()][coord.get_x()] = 's';
            coord.dec_x();
        }
        coord.dec_x();
    }

    coord = {0, FIELD_SIZE - 2};
    for (std::size_t i = 0; i < 2; i++) { //set 1 x 4 small bun
        for (std::size_t j = 0; j < 2; j++) {
            field[coord.get_y() + i][coord.get_x() + j] = 's';
        }
    }

    coord.dec_y();
    coord.dec_y();
    for (std::size_t i = 0; i < 4; i++) { //set 1 x 4 longboi
        field[coord.get_y() - i][coord.get_x()] = 's';
    }

    coord = {0, 0};
    for (std::size_t i = 0; i < 3; i++) { // set 1 x 6 big bun
        for (std::size_t j = 0; j < 2; j++) {
            field[coord.get_y() + i][coord.get_x() + j] = 's';
        }
    }

    coord = {3, 0};
    for (std::size_t i = 0; i < 3; i++) { //set 3 x 1 ships
        field[coord.get_y()][coord.get_x() + i * 2] = 's';
    }

    field[FIELD_SIZE / 2][FIELD_SIZE / 2] = 's'; //set 1 x 1 ship_imposter
}