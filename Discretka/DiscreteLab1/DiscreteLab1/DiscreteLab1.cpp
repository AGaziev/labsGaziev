#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

class CharSet
{

public:
    //construct based on vector<char>
    CharSet() { m_size = 0, m_data = {}; };
    CharSet(vector<char> data)
    {
        sort(data.begin(), data.end());
        m_data = data;
        m_size = data.size();
        eraseNull();
    }

#pragma region ПЕРЕГРУЗКА ОПЕРАТОРОВ;
    CharSet operator+(CharSet other) {
        int unionSize = m_data.size() + other.getData().size();
        vector<char> tmp(26);
        set_union(m_data.begin(), m_data.end(), other.m_data.begin(), other.m_data.end(), tmp.begin());
        CharSet tmpClass(tmp);
        return tmpClass;
    }

    CharSet operator*(CharSet other) {
        int unionSize = m_data.size() + other.getData().size();
        vector<char> tmp(26);
        set_intersection(m_data.begin(), m_data.end(), other.m_data.begin(), other.m_data.end(), tmp.begin());
        CharSet tmpClass(tmp);
        return tmpClass;
    }

    CharSet operator-(CharSet other) {
        int unionSize = m_data.size() + other.getData().size();
        vector<char> tmp(26);
        set_difference(m_data.begin(), m_data.end(), other.m_data.begin(), other.m_data.end(), tmp.begin());
        CharSet tmpClass(tmp);
        return tmpClass;
    }

    CharSet operator!() {
        vector<char> tmp(26);
        set_difference(uniSet.begin(), uniSet.end(), m_data.begin(), m_data.end(), tmp.begin());
        CharSet tmpClass(tmp);
        return tmpClass;
    }

    bool operator==(CharSet other)
    {
        int unionSize = m_data.size() + other.getData().size();
        vector<char> tmp(26);
        set_union(m_data.begin(), m_data.end(), other.m_data.begin(), other.m_data.end(), tmp.begin());
        if (tmp == m_data && tmp == other.getData())
        {
            return true;
        }
        else return false;
    }

    void operator=(CharSet other)
    {
        other.eraseNull();
        eraseNull();
        this->m_size = other.getSize();
        this->m_data = other.m_data;
    }
#pragma endregion or,and,not,notUni,isEqual,Equal;

    vector<char> getData()
    {
        return m_data;
    }
    int getSize()
    {
        return m_size;
    }

    void print()
    {
        eraseNull();
        if (m_data.empty())
        {
            cout << "EMPTY\n";
            return;
        }
        for (int i = 0; i < m_data.size(); i++)
        {
            if (m_data[i] != '\0')
                cout << m_data[i] << " ";
        }
        cout << endl;
    }

    

    vector<char> m_data = {};

private:
    int m_size = 0;
    const vector<char>  uniSet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    void eraseNull()
    {
        for (int i = 0; i < m_data.size(); i++)
        {
            if (m_data[i] == '\0')
            {
                m_data.erase(m_data.begin() + i);
                i--;
            }
        }
    }
};

CharSet InitClass()
{
    vector<char> tempV={};
    char temp;

    while(cin>>temp)
    {
        if (temp != '0')
            tempV.push_back(temp);
        else break;
    }
    return tempV;
}

int main()
{   
    setlocale(LC_ALL, "Russian");
    //ИНИЦИАЛИЗАЦИЯ МНОЖЕСТВ
    cout << "Введите множество А(0 для конца):"<<endl;
    CharSet A(InitClass());
    cout << "Введите множество B(0 для конца):" << endl;
    CharSet B(InitClass());
    cout << "Введите множество C(0 для конца):" << endl;
    CharSet C(InitClass());
    //ПУСТОЕ МНОЖЕСТВО
    vector<char> Empty = {};
    CharSet emptySet(Empty);
    //МАССИВ МНОЖЕСТВ
    CharSet arr[3] = { A,B,C };
    //ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС
    while (true)
    {
        int choosed[2] = { 0,0 };
        cout << "Введите названия двух множеств с которыми необходимо провести операции (A B C): ";
        for (int i = 0; i < 2; i++)
        {
            char temp;
            cin >> temp;
            choosed[i] = temp-65;
        }
        cout << "Введите операцию ('-' - не, '+' - или, '*' - и, '=' - равны, другое для задания варианта): ";
        char temp=' ';
        bool fExit = false;
        cin >> temp;
        switch (temp)
        {
            case '-':
                arr[choosed[0]].print();
                arr[choosed[1]].print();
                (arr[choosed[0]] - arr[choosed[1]]).print();
                break;
            case '+':
                arr[choosed[0]].print();
                arr[choosed[1]].print();
                (arr[choosed[0]] + arr[choosed[1]]).print();
                break;
            case'*':
                arr[choosed[0]].print();
                arr[choosed[1]].print();
                (arr[choosed[0]] * arr[choosed[1]]).print();
                break;
            case '=':
                arr[choosed[0]].print();
                arr[choosed[1]].print();
                if (arr[choosed[0]] == arr[choosed[1]])
                    cout << true;
                else cout << false;
                break;
            default:
                fExit=true;
                break;
        }
        if (fExit)
            break;

    }
    //ЗАДАНИЕ ВАР16 ЛАБ1 ГАЗИЕВ 2ПМ
    cout << "B U ( A \\ B ) = A U B\n";
    (B + (A - B)).print();  cout << "=\n"; (A + B).print();
    cout << "B * ( A \\ B ) = 0\n";
    (B * (A - B)).print();  cout << "=\n"; emptySet.print();
    cout << "( A \\ B ) * B = 0\n";
    ((A - B) * B).print();  cout << "=\n"; emptySet.print();
    cout << "A \\ B = A \\ ( A * B )\n";
    (A - B).print();        cout << "=\n"; (A - (A * B)).print();
    cout << "A * ( B * C ) = ( A * B ) U ( A * C )\n";
    (A * (B + C)).print();  cout << "=\n"; ((A * B) + (A * C)).print();
}


