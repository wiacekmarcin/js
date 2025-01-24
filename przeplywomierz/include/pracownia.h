
class Adafruit_MCP23017;

class Pomieszczenie {

    public:
    void setWieczor(bool wie) { wieczor = wie; };
    void setNoc(bool n) { noc = n; };
    void setTaryfa2(bool t2) { taryfa2 = t2; };
    void setZasilanieAwaryjne(bool zasaw) { zasilAwar = zasaw; };

    void setInput(int in1, int in2) { };
    protected:
    bool wieczor;
    bool noc;
    bool taryfa2;
    bool zasilAwar;
};

class Pracownia : public Pomieszczenie
{

public:
    Pracownia( Adafruit_MCP23017 * e) {
        exp = e;
    }

    void zapal1(bool on = true);
    void zapal2(bool on = true);
    void off();
    void setInput(int in1, int in2);  

private:
    Adafruit_MCP23017 * exp;
};