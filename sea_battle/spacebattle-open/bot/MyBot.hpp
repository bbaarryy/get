// This is your Bot.
#pragma once
#include "Bot.hpp"
#include <vector>
#include <chrono>
#include <ctime>
#include <thread>
#include <random>
#include <iostream>
#include <fstream>



class MyBot: public Bot {
private:

    std::vector<Point> pointers;
    bool is_killing;

     
    
    Point hitting_group_mass[169];
    int hit_i = 0;
    
    std::vector<std::vector<char>> sea;

    int curr_step = 4;
    int turns = 0;

public:

    bool dot_is_correct(std::vector<std::vector<char>>& my_field,int x,int y){
        bool ch = 0;
        if(my_field[x][y] == 'o'){
            if(x>0 && my_field[x-1][y] != 'o'){ch=1;}
            if(y>0 && my_field[x][y-1] != 'o'){ch=1;}
            if(x>0 && y>0 && my_field[x-1][y-1] != 'o'){ch=1;}
            if(x>0 && y<12 && my_field[x-1][y+1] != 'o'){ch=1;}
            if(x<12 && y>0 && my_field[x+1][y-1] != 'o'){ch=1;}
            if(x<12 && y<12 && my_field[x+1][y+1] != 'o'){ch=1;}
            if(y<12 && my_field[x][y+1] != 'o'){ch=1;}
            if(x<12 && my_field[x+1][y] != 'o'){ch=1;}
        }
        else{ch=1;}

        return (!ch);
    }

    void spawn_single(std::vector<std::vector<char>>& my_field){
        int curr = rand()%169;
        while(true){
            curr = rand()%169;
            int x = curr/13;
            int y = curr%13;
            bool ch = 0;
            if(my_field[x][y] == 'o'){
                if(x>0 && my_field[x-1][y] != 'o'){ch=1;}
                if(y>0 && my_field[x][y-1] != 'o'){ch=1;}
                if(x>0 && y>0 && my_field[x-1][y-1] != 'o'){ch=1;}
                if(x>0 && y<12 && my_field[x-1][y+1] != 'o'){ch=1;}
                if(x<12 && y>0 && my_field[x+1][y-1] != 'o'){ch=1;}
                if(x<12 && y<12 && my_field[x+1][y+1] != 'o'){ch=1;}
                if(y<12 && my_field[x][y+1] != 'o'){ch=1;}
                if(x<12 && my_field[x+1][y] != 'o'){ch=1;}
                if(!ch){my_field[x][y] = 's';return ;}
            }
        }
    }
    
    void spawn_double(std::vector<std::vector<char>>& my_field){
        int curr = rand()%169;
        int orient = rand()%2;
        while(true){
            curr = rand()%169;
            int x = curr/13;
            int y = curr%13;
            if(orient == 1){
                if(x>0 && dot_is_correct(my_field,x,y) && dot_is_correct(my_field,x-1,y)){
                    my_field[x][y] = 's';my_field[x-1][y] = 's';return;
                }
                else if(x<12 && dot_is_correct(my_field,x,y) && dot_is_correct(my_field,x+1,y)){
                    my_field[x][y] = 's';my_field[x+1][y] = 's';return;
                }
            }
            else{
                if(y>0 && dot_is_correct(my_field,x,y) && dot_is_correct(my_field,x,y-1)){
                    my_field[x][y] = 's';my_field[x][y-1] = 's';return;
                }
                else if(y<12 && dot_is_correct(my_field,x,y) && dot_is_correct(my_field,x,y+1)){
                    my_field[x][y] = 's';my_field[x][y+1] = 's';return;
                }
            }
        }
    }

    void deploy(Field& field) override{
        srand(std::time(0));
        std::vector<std::vector<char>> my_field(13, std::vector<char> (13,'o'));

        std::vector<int> a = {1,2,3,4,5};

        //without single ships
        my_field = {{'o','o','s','s','o','o','o','o','o','o','o','o','o'},
                    {'o','o','s','s','o','o','o','o','o','o','o','o','o'},
                    {'o','o','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','s','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','s','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','s','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','o','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','o','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','s','o','s','s','s','s','o','o','o','o','o','o'},
                    {'o','s','o','o','o','o','o','o','o','o','o','o','o'},
                    {'o','s','o','o','o','o','o','o','s','s','o','o','o'},
                    {'o','o','o','o','o','o','o','o','s','s','o','o','o'},
                    {'o','o','o','o','o','o','o','o','s','s','o','o','o'}};
        
        spawn_double(my_field);
        spawn_double(my_field);
        spawn_double(my_field);
        
        spawn_single(my_field);
        spawn_single(my_field);
        spawn_single(my_field);
        spawn_single(my_field);
        
        for(int x = 0 ; x < 13;x++){
            for(int y = 0 ; y < 13 ; y ++){
                field[x][y] = my_field[x][y];
            }
        }
    };

    Point find_where_to_kill(Point* hitting_group){
        for(int i = 0 ; i < hit_i;i++){
            int x = hitting_group[i].get_x();
            int y = hitting_group[i].get_y();

            if(x > 0 && sea[x-1][y] == '.'){
                return {x-1,y};
            }
            if(y > 0 && sea[x][y-1] == '.'){
                return {x,y-1};
            }
            if(x < 12  && sea[x+1][y] == '.'){
                return {x+1,y};
            }
            if(y < 12 && sea[x][y+1] == '.'){
                return {x,y+1};
            }
        }
        return {0,0};
    }

    void clear_around_area(Point* hitting_group){
        for(int i = 0 ; i < hit_i;i++){
            int x = hitting_group[i].get_x();
            int y = hitting_group[i].get_y();

            if(x > 0 && y>0 && sea[x-1][y-1] == '.'){
                sea[x-1][y-1] = 'o';
            }
            if(x < 12 && y<12 && sea[x+1][y+1] == '.'){
                sea[x+1][y+1] = 'o';
            }
            if(x > 0 && y<12 && sea[x-1][y+1] == '.'){
                sea[x-1][y+1] = 'o';
            }
            if(x < 12 && y>0 && sea[x+1][y-1] == '.'){
                sea[x+1][y-1] = 'o';
            }
            

            if(x > 0 && sea[x-1][y] == '.'){
                sea[x-1][y] = 'o';
            }
            if(y > 0 && sea[x][y-1] == '.'){
                sea[x][y-1] = 'o';
            }
            if(x < 12  && sea[x+1][y] == '.'){
                sea[x+1][y] = 'o';
            }
            if(y < 12 && sea[x][y+1] == '.'){
                sea[x][y+1] = 'o';
            }
        }
    }

    Point get_new(int step){
        //std::cout << "curr_step: "<<step<<'\n';
        if(step == -1){
            int curr = rand()%169;
            //std::cout << "curr_rand: " << curr << '\n';
            while(sea[curr/13][curr%13] != '.'){
                curr = rand()%169;
            }
            return {curr/13, curr%13};
        }
        else{
        for(int i = 0 ; i < 13 ; i ++){
            for(int j = i*13%step ; j < 13 ; j +=step){
                if(sea[i][j] == '.'){
                    return {i,j};
                }
            }
        }
        return {100,100};}
    }   

    Point shoot(ShotResult previousShot) override{
        turns++;
        //if(turns > 60){curr_step=3;}//or maybe RANDOM
        if(turns > 80){curr_step=-1;}//or maybe RANDOM
        if(previousShot != WIN && previousShot != FIRST_TURN){
            if(previousShot == HIT){
                //std::cout << "start_hit" << '\n';
                //std::cout << sea.size() << '\n';
                //std::cout << sea[0].size() << '\n';
                is_killing = 1;

                hitting_group_mass[hit_i] = pointers.back();
                hit_i++;

                Point curr = pointers.back();
                //std::cout << curr.get_x() << ' ' << curr.get_y() << '\n';
                sea[curr.get_x()][curr.get_y()] = 's';
                //std::cout << "pik_sea" << '\n';
                ///find near area to HIT
                Point XXX = find_where_to_kill(hitting_group_mass);

                pointers.push_back(XXX);
                return XXX;
            }
            else if(previousShot == KILL){
                is_killing = 0;

                hitting_group_mass[hit_i] = pointers.back();
                hit_i++;

                Point curr = pointers.back();
                sea[curr.get_x()][curr.get_y()] = 's';

                clear_around_area(hitting_group_mass);
                hit_i=0;

                auto XXX = get_new(curr_step);
                while(XXX.get_x() == 100){
                    curr_step--;
                    if(curr_step == -2){curr_step = -1;}
                    XXX = get_new(curr_step);
                }
                pointers.push_back(XXX);
                return XXX;
            }
            else if(previousShot == MISS){
                if(is_killing){
                    Point curr = pointers.back();
                    sea[curr.get_x()][curr.get_y()] = 'o';
                    Point XXX = find_where_to_kill(hitting_group_mass);
                    
                    pointers.push_back(XXX);
                    return XXX;
                }
                else{
                    Point curr = pointers.back();
                    sea[curr.get_x()][curr.get_y()] = 'o';
                    
                    auto XXX = get_new(curr_step);
                    //std::cout << "recieved" << '\n';
                    while(XXX.get_x() == 100){
                        curr_step--;
                        if(curr_step == -2){curr_step = -1;}
                        XXX = get_new(curr_step);
                    }
                    //std::cout << "Find new target" << '\n';
                    pointers.push_back(XXX);
                    
                    //std::cout << "Sending: " << XXX.get_x() << ' ' << XXX.get_y() << '\n';

                    return XXX;
                }
            }
        }
        else if(previousShot == FIRST_TURN){
            for(int i = 0 ; i < 13 ; i ++){
                std::vector<char> curr;
                for(int j = 0 ; j < 13;j++){
                    curr.push_back('.');  
                }
                (sea).push_back(curr);
            }
            is_killing = 0;
            
            pointers.push_back({1,1});
            return {1,1};
        }
        else{
            pointers.push_back({1,1});
            return {1,1};
        }
        pointers.push_back({0,0});
        return {12,12};
    };
};