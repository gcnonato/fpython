from urllib import robotparser

robot_parser = robotparser.RobotFileParser()

def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)
    robot_parser.read()


def is_allowed(target_url, user_agent='*'):
    return robot_parser.can_fetch(user_agent, target_url)


if __name__ == '__main__':
    prepare('http://www.sindasp.org.br/robots.txt')

    print(is_allowed('http://www.sindasp.org.br/site/agenda.php/', 'bookbot'))
    print(is_allowed('http://www.sindasp.org.br/site/agenda.php/', 'my - agent'))
    print(is_allowed('http://www.sindasp.org.br/site/agenda.php/', 'googlebot'))
