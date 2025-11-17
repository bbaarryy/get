void separate_odd_even(const Sequence* input, Sequence** odd, Sequence** even){
    Sequence* a;
    a->data = new int[input->size];
    int* na;
    na = new int;
    a->size = *na;

    Sequence* b;
    b->data = new int[input->size];
    int* nb;
    nb = new int;
    b->size = *nb;
    
    *odd = a;
    *even = b;
    
    int even_size=0;
    int odd_size = 0;

    int il = 0;
    int ir = 0;
    for(int i = 0 ; i < input->size ; i++){
        if((input->data)[i] % 2 == 1){
            (*odd)->data[il] = (input->data)[i];
            odd_size++;
            il++;
        }
        else{
           (*even)->data[ir] = (input->data)[i];
            even_size++;
            ir++;
        }
    }
    
    (**odd).size = odd_size;
    (**even).size = even_size;
}

void clear(Sequence* s){
    
    delete[] s->data;
}