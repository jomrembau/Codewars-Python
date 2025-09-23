def past(h, m, s):
    h_milli = h * 3600000
    m_milli = m * 60000
    s_milli = s * 1000
    answer =  h_milli + m_milli + s_milli
    return answer


print(past(0,1,1))