import math

class Transmigration:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        pw = java.io.PrintWriter(System.out)
        st = java.util.StringTokenizer(br.readLine())
        n = int(st.nextToken())
        m = int(st.nextToken())
        k = int(st.nextToken().substring(2))
        skills = {}
        for i in range(0, n):
            st = java.util.StringTokenizer(br.readLine())
            skillName = st.nextToken()
            skillScore = int(st.nextToken())
            newSkillScore = math.trunc(skillScore * k / float(100))
            if newSkillScore < 100:
                continue
            skills[skillName] = newSkillScore
        for i in range(0, m):
            skillName = br.readLine()
            if skillName in skills.keys():
                continue
            skills[skillName] = 0
        pw.println(len(skills))
        for skill in skills.entrySet():
            pw.println(skill.getKey() + " " + skill.getValue())
        pw.flush()
        pw.close()
