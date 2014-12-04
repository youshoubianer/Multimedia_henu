/*
*   arithmetic encoding
*   lang:c++
*
*   ���ַ����ܳ�ʱ����һЩ����Ľ�����....
*/


#include <iostream>
#include<fstream>
#include<algorithm>
using namespace std;
typedef struct ch
{
    char charactor;
    int times;
    double p;
    double start;
    double ends;
} ch;
ch c[1000];
string str;
int len,k;
double startN,startA,temp,endN,endA;

void init()
{
    for(int i=0; i<1000; i++)
    {
        c[i].charactor='\0';
        c[i].ends=1;
        c[i].start=0;
        c[i].times=0;
    }
}
bool cmp(ch a,ch b)
{
    if(a.p>b.p)
        return true;
    if (a.charactor<b.charactor)
        return true;
    return false;
}
ch find_se(char x)
{
    for(int i=0; i<k; i++)
    {
        if(c[i].charactor==x)
            return c[i];
    }
}

void get_p()
{
    len = str.length();
    k=0;
    //ͳ�Ƹ���
    for(int i=0; i<len; i++)
    {
        bool f = false;
        for(int j=0; j<k; j++)
        {
            if(c[j].charactor==str[i])
            {
                c[j].times++;
                f = true;
                break;
            }
        }
        if(!f)
        {
            c[k].charactor=str[i];
            c[k].times++;
            k++;
        }
    }
    //����
    sort(c,c+k,cmp);
}
void encoding()
{
    //  ��������
    for(int i=0; i<k; i++)
    {
        c[i].p=(1.0/((double)len))*(double)c[i].times;
        c[i].start=c[i-1].ends;
        c[i].ends = c[i].start+c[i].p;
    }
    //encoding
    startN = 0;
    endN = 1.0;
    for(int i=0; i<len; i++)
    {
        startA = find_se(str[i]).start;
        endA = find_se(str[i]).ends;
        temp = startN+startA*(endN-startN);
        endN = startN+endA*(endN-startN);
        startN = temp;
    }
}

string unzip(double coding)
{
    string unzip_string="";
    //find_ch();
    startN = 0;
    endN = 1.0;
    double tempS,tempN;
    for(int j=0; j<len; j++)
    {
        for(int i=0; i<k; i++)
        {
            startA = c[i].start;
            endA = c[i].ends;
            tempS = startN+startA*(endN-startN);
            tempN = startN+endA*(endN-startN);

            if(coding>=tempS&&coding<tempN)
            {
                unzip_string+=c[i].charactor;
                startN = tempS;
                endN = tempN;
                break;
            }
        }
    }
    return unzip_string;
}
int main()
{
    //freopen("in.in","r",stdin);
    while(getline(cin,str))
    {
        init(); //��ʼ��...
        get_p();//��ȡ����...
        encoding();//����...
        cout<<"��������: ("<<startN<<","<<endN<<")"<<endl;
        cout<<"����������: "<<startN<<endl;

        //����...
        string unzip_result = unzip(startN);
        cout<<"������: "<<unzip_result<<endl;
    }
    return 0;
}
