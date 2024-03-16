import math


class ElectricSystem:
    def __init__(self, p, un, w1, w2, k01, k02, r1, r2, x1, x2, m1, m2, poles, f1, ns, sn):
        self.p = p
        self.un = un
        self.w1 = w1
        self.w2 = w2
        self.k01 = k01
        self.k02 = k02
        self.r1 = r1
        self.r2 = r2
        self.x1 = x1
        self.x2 = x2
        self.m1 = m1
        self.m2 = m2
        self.poles = poles
        self.f1 = f1
        self.ns = ns
        self.sn = sn

    def calculate(self):
        ke = round((self.k01 * self.w1) / (self.k02 * self.w2), 3)
        k1 = round((self.m1 * self.k01 * self.w1) / (self.m2 * self.k02 * self.w2), 3)
        r2_1 = round(ke * k1 * self.r2, 3)
        x2_1 = round(ke * k1 * self.x2, 3)
        r_k = round(self.r1 + r2_1, 3)
        x_k = round(self.x1 + x2_1, 3)
        z_k = round(math.sqrt(r_k ** 2 + x_k ** 2), 3)
        i_1n = round(self.un / z_k, 3)
        i_2n = round(i_1n * k1, 3)
        m_it = round((self.poles * self.m1 * self.un ** 2 * r2_1) / (2 * math.pi * self.f1 * (r_k ** 2 + x_k ** 2)), 3)
        cosf_n = round(r_k / z_k, 3)
        s_kr = round(r2_1 / (math.sqrt(self.r1 ** 2 + x_k ** 2)), 3)
        m_cher = round((1 + s_kr ** 2) / (2 * s_kr), 3)
        m = round(m_cher, 3)
        s_pog34 = round(s_kr, 3)
        s_pog23 = round((s_pog34 ** 2) ** (1 / 3), 3)
        s_pog12 = round(math.sqrt(s_pog23), 3)
        r_1dob = round(r2_1 * ((m_cher / (m * s_kr)) - 1), 3)
        r_dob = round(r_1dob / (ke * k1), 3)
        r_1dob1 = round((r2_1 + r_1dob) * (1 - s_pog12), 3)
        r_dob1 = round(r_1dob1 / (ke * k1), 3)
        r_1dob2 = round((r2_1 + r_1dob) * (1 - s_pog23) - r_1dob1, 3)
        r_dob2 = round(r_1dob2 / (ke * k1), 3)
        r_dob3 = round(r_dob - r_dob1 + r_dob2, 3)
        i1n = round(self.un / (math.sqrt((self.r1 + r2_1 + r_1dob) ** 2 + x_k ** 2)), 3)
        i2n = round(i1n * k1, 3)
        mn = round((self.poles * self.m1 * self.un ** 2 * (r2_1 + r_1dob)) / (
                    2 * math.pi * self.f1 * (r_k + r_1dob) ** 2 + x_k ** 2), 3)
        cosfn = round((r_k + r_1dob) / (math.sqrt((r_k + r_1dob) ** 2 + x_k ** 2)), 3)
        s1 = round((self.sn * (self.r2 + r_dob1)) / self.r2, 3)
        n1 = round(self.ns * (1 - s1), 3)
        s2 = round((self.sn * (self.r2 + r_dob2 + r_dob3)) / self.r2, 3)
        n2 = round(self.ns * (1 - s2), 3)
        s3 = round((self.sn * (self.r2 + r_dob3)) / self.r2, 3)
        n3 = round(self.ns * (1 - s3), 3)
        n = round(self.ns * (1 - self.sn), 3)
        results_list = {
            "ke": ke,
            "k1": k1,
            "r2_1": r2_1,
            "x2_1": x2_1,
            "r_k": r_k,
            "x_k": x_k,
            "z_k": z_k,
            "i_1n": i_1n,
            "i_2n": i_2n,
            "m_it": m_it,
            "cosf_n": cosf_n,
            "s_kr": s_kr,
            "m_cher": m_cher,
            "m": m,
            "s_pog34": s_pog34,
            "s_pog23": s_pog23,
            "s_pog12": s_pog12,
            "r_1dob": r_1dob,
            "r_dob": r_dob,
            "r_1dob1": r_1dob1,
            "r_dob1": r_dob1,
            "r_1dob2": r_1dob2,
            "r_dob2": r_dob2,
            "r_dob3": r_dob3,
            "i1n": i1n,
            "i2n": i2n,
            "mn": mn,
            "cosfn": cosfn,
            "s1": s1,
            "n1": n1,
            "s2": s2,
            "n2": n2,
            "s3": s3,
            "n3": n3,
            "n": n
        }
        return results_list


electric_system = ElectricSystem(15, 220, 192, 36, 0.932, 0.955, 0.46, 0.02, 2.24, 0.08, 3, 3, 3, 50, 1000, 0.04)
results = electric_system.calculate()
for key, value in results.items():
    print(f"{key}: {value}")
