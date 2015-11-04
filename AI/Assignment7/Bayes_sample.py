#!/usr/bin/python

import Queue
import sys #for command line args
import math
import numpy as np
from lib_matt import printV

class prior_sampling():

    def __init__(self):
        self.samples = np.array( [[0.82,  0.56,  0.08,  0.81],[0.34,  0.22,  0.37,  0.99],
                            [0.55,  0.61,  0.31,  0.66], [0.28,  1.00,  0.95,  0.71],
                            [0.14,  0.10,  1.00,  0.71], [0.10,  0.60,  0.64,  0.73],
                            [0.39,  0.03,  0.99,  1.00], [0.97,  0.54,  0.80,  0.97],
                            [0.07,  0.69,  0.43,  0.29], [0.61,  0.03,  0.13,  0.14],
                            [0.13,  0.40,  0.94,  0.19], [0.60,  0.68,  0.36,  0.67],
                            [0.12,  0.38,  0.42,  0.81], [0.00,  0.20,  0.85,  0.01],
                            [0.55,  0.30,  0.30,  0.11], [0.83,  0.96,  0.41,  0.65],
                            [0.29,  0.40,  0.54,  0.23], [0.74,  0.65,  0.38,  0.41],
                            [0.82,  0.08,  0.39,  0.97], [0.95,  0.01,  0.62,  0.32],
                            [0.56,  0.68,  0.32,  0.27], [0.77,  0.74,  0.79,  0.11],
                            [0.29,  0.69,  0.99,  0.79], [0.21,  0.20,  0.43,  0.81],
                            [0.90,  0.00,  0.91,  0.01]]);
        # check self.samples is stored correctly
        for i in self.samples:
            printV(["given self.samples: ", i],0);

        # Im not sure if this is how im supposed to use the given self.samples

        # There are 4 nodes and 100 self.samples so there will be 25 complete iterations
        self.cpt = {"cloudy":[0.5],"sprinkler":[0.1,0.5],"rain":[0.8,0.2],"wet":[0.99,0.90,0.90,0.00]}

        self.dict_array = [];

        # set the dictionary for each complete iteration and append
        # to dict_array
        for sample_temp in self.samples:
            self.set_sample_dict(sample_temp)

        self.dict_array = np.array(self.dict_array);
        for i in range(0,25):
            printV([i,":  ",self.dict_array[i]],1);
    # ...






    # if check is greater than mark return false
    def check_mark(self,check,mark):
        printV(["check",check],1);
        printV(["mark",mark],1);
        if (check <= mark):
            return True;
        else: return False;
    # ...

    def set_sample_dict(self,sample_array):
        temp_dict = {};
        #check cloudy
        if (self.check_mark(sample_array[0],self.cpt['cloudy'][0]))is True:
            printV("it is cloudy",1);
            # set the cloudy value in
            temp_dict['cloudy'] = True;
        else:
            printV("it is not cloudy",1);
            # set the cloudy value in
            temp_dict['cloudy'] = False;

        # check sprinkler
        if (temp_dict['cloudy']) is True:
            # cloudy is true so look at sprinkler[0]
            if (self.check_mark(sample_array[1],self.cpt['sprinkler'][0]))is True:
                printV("cloudy is true and sprinkler is true",1);
                temp_dict['sprinkler'] = True;
            else:
                printV("cloudy is true and sprinkler is false",1);
                temp_dict['sprinkler'] = False;
        else:
            # cloudy is false so look at sprinkler[1]
            if (self.check_mark(sample_array[1],self.cpt['sprinkler'][1]))is True:
                printV("cloudy is false and sprinkler is true",1);
                temp_dict['sprinkler'] = True;
            else:
                printV("cloudy is false and sprinkler is false",1);
                temp_dict['sprinkler'] = False;

        # check rain
        if (temp_dict['cloudy']) is True:
            # cloudy is true so look at rain[0]
            if (self.check_mark(sample_array[2],self.cpt['rain'][0]))is True:
                printV("cloudy is true and rain is true",1);
                temp_dict['rain'] = True;
            else:
                printV("cloudy is true and rain is false",1);
                temp_dict['rain'] = False;
        else:
            # cloudy is false so look at rain[1]
            if (self.check_mark(sample_array[2],self.cpt['rain'][1]))is True:
                printV("cloudy is false and rain is true",1);
                temp_dict['rain'] = True;
            else:
                printV("cloudy is false and rain is false",1);
                temp_dict['rain'] = False;

        #check wet grass
        if ((temp_dict['sprinkler'])is True and (temp_dict['rain'])is True):
            printV("true true",1);
            # use wet[0]
            if (self.check_mark(sample_array[3],self.cpt['wet'][0]))is True:
                printV("cloudy is false and wet is true",1);
                temp_dict['wet'] = True;
            else:
                printV("cloudy is false and wet is false",1);
                temp_dict['wet'] = False;
        elif ((temp_dict['sprinkler'])is True and (temp_dict['rain'])is False):
            printV("true false",1);
            # use wet[1]
            if (self.check_mark(sample_array[3],self.cpt['wet'][1]))is True:
                printV("cloudy is false and wet is true",1);
                temp_dict['wet'] = True;
            else:
                printV("cloudy is false and wet is false",1);
                temp_dict['wet'] = False;
        elif ((temp_dict['sprinkler'])is False and (temp_dict['rain'])is True):
            printV("false true",1);
            # use wet[2]
            if (self.check_mark(sample_array[3],self.cpt['wet'][2]))is True:
                printV("cloudy is false and wet is true",1);
                temp_dict['wet'] = True;
            else:
                printV("cloudy is false and wet is false",1);
                temp_dict['wet'] = False;
        elif ((temp_dict['sprinkler'])is False and (temp_dict['rain'])is False):
            printV("false false",1);
            # use wet[3]
            if (self.check_mark(sample_array[3],self.cpt['wet'][3]))is True:
                printV("cloudy is false and wet is true",1);
                temp_dict['wet'] = True;
            else:
                printV("cloudy is false and wet is false",1);
                temp_dict['wet'] = False;

        self.dict_array.append(temp_dict);
    # ...


    def prior_marginal_prob(self,key):
        # calculate the number of entries where key is true
        # divide by numnber of complete iterations (25)
        true_count = 0;
        false_count = 0;
        for i in range(0,25):
            if (self.dict_array[i][key])is True:
                true_count = true_count + 1;
            else:
                false_count = false_count + 1;
        printV(true_count,1);
        printV(false_count,1);
        return np.array([float(true_count)/25,float(false_count)/25]);
    # ...



    def prior_conditional_prob(self,find_val,given_list):
        printV(["find value",find_val],1);
        printV(["given list",given_list],1);
        # need to calculate the total number of eqations that satisfy the
        # given list

        cond_array = [];

        [(find_key,find_value)] = find_val.items();
        printV(["find_key: ",find_key,"  find_value: ",find_value],1);

        # valid array is the array of currently valid complete samples
        valid_array = self.dict_array;
        # find all complete samples which satisfy all of the givens
        for given_temp in given_list:
            given_sample_number = 0;
            [(given_key, given_value)] = given_temp.items();
            # temp_array stores complete samples from valid array that
            # satisfy the new given
            temp_array = [];
            printV(["given_key: ",given_key,"  given_value: ",given_value],1);
            for i in range(len(valid_array)):
                if (valid_array[i][given_key] == given_value)is True:
                    given_sample_number = given_sample_number + 1;
                    temp_array.append(valid_array[i]);
            valid_array = temp_array;
        cond_array = np.array(valid_array);
        printV(["given_sample_number: ",given_sample_number],1);
        for i in range(0,given_sample_number):
            printV([i," :",cond_array[i]],1);


        # calculate the number of equations where find_value is <true,false> from within the
        # above list and divide by the total number of eq in the above list
        find_value_cnt = 0;
        not_find_value_cnt = 0;
        for i in range(0,given_sample_number):
            if (cond_array[i][find_key] == find_value)is True:
                find_value_cnt = find_value_cnt + 1;
            else:
                not_find_value_cnt = not_find_value_cnt +1;
        return np.array([float(find_value_cnt)/given_sample_number,
                         float(not_find_value_cnt)/given_sample_number]);
    # ...
























def main():

    ps = prior_sampling();
    # ready to start computing prob
    printV("Problem 1: Prior sampling",2);
    cloudy_marg = ps.prior_marginal_prob("cloudy");
    printV(["a.  P(c = True): ",cloudy_marg[0]],2);
    cond_returned = ps.prior_conditional_prob({'cloudy':True,},[{'rain':True}]);
    printV(["b.  P(c = True | rain = True): ",cond_returned[0]],2);
    cond_returned = ps.prior_conditional_prob({'sprinkler':True,},[{'wet':True}]);
    printV(["c.  P(s = True | w = True): ",cond_returned[0]],2);
    cond_returned = ps.prior_conditional_prob({'sprinkler':True,},[{'cloudy':True},{'wet':True}]);
    printV(["d.  P(s = True | c = True, w = True): ",cond_returned[0]],2);
if __name__ == "__main__":
    main()
