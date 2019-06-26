from dataclasses import dataclass

@dataclass
class User():
    username: str
    name: str
    title: str
    position: str
    summary: str
    skills: str
    experience: int
    education: int

    def get_data_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'title': self.title,
            'position': self.position,
            'summary': self.summary,
            'skills': self._get_skill_list(),
            'experience': self.experience,
            'education': self.education,
            'score': self._get_score()
        }

    def _get_skill_list(self):
        try:
            skill_list = self.skill_list
        except AttributeError:
            skill_list = self._make_skill_list()
            self.skill_list = skill_list
        return skill_list
    
    def _make_skill_list(self):
        return self.skills.split(',')

    def _get_score(self):
        try:
            score = self.score
        except AttributeError:
            score = self._calculate_score()
            self.score = score
        return score
            
    def _calculate_score(self):
        return self.experience + self.education

