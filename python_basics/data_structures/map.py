#!/usr/bin/env python3

m_km = lambda x: x * 1000

meters = [2, 4, 4, 5, 7, 1]
res = list(map(m_km, meters))
print(res)
