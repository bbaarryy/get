#include <iostream>
#include <algorithm>

using namespace std;

class Material  
{
public:
    // Принимает на вход величину деформации.
    // Возвращает величину напряжения, посчитанную с учётом реологии материала.
    virtual float getStress(float strain) = 0;
};

class ElasticMaterial: public Material
{
public:
    float M;
    ElasticMaterial(float elasticModulus);
    float getStress(float strain) = 0;
};

ElasticMaterial::ElasticMaterial(float elasticModulus){
    this->M = elasticModulus;
}

float ElasticMaterial::getStress(float strain){
    return strain*this->M;
}

class PlasticMaterial: public Material
{
public:
    float M,L;
    PlasticMaterial(float elasticModulus, float strainLimit);
    float getStress(float strain);
};

PlasticMaterial::PlasticMaterial(float elasticModulus, float strainLimit){
    this->M = elasticModulus;
    this->L = strainLimit;
}

float PlasticMaterial::getStress(float strain){
    return max(this->L, strain * this->M);
}


int main(){
    

}