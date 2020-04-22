import os
import pytest
from subprocess import check_output
from conftest import system_check


def no_curlies(filepath):
    """ Utility to make sure no curly braces appear in a file.
        That is, was jinja able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.path
        if pytest.param.get('project_name'):
            name = system_check('DrivenData')
            assert project.name == name
        else:
            assert project.name == 'project_name'

    def test_author(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--author']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('author_name'):
            assert p == 'DrivenData'
        else:
            assert p == 'Your name (or your organization/company/team)'

    def test_readme(self):
        readme_path = self.path / 'README.md'
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get('project_name'):
            with open(readme_path) as fin:
                assert '# DrivenData' == next(fin).strip()

    def test_setup(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--version']
        p = check_output(args).decode('ascii').strip()
        assert p == '0.1.0'
        assert no_curlies(setup_)

    def test_name(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--name']
        p = check_output(args).decode('ascii').strip()
        library_name = pytest.param.get('library_name', 'core')
        assert p == library_name

    def test_license(self):
        license_path = self.path / 'LICENSE'
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        setup_ = self.path / 'setup.py'
        args = ['python', setup_, '--license']
        p = check_output(args).decode('ascii').strip()
        if pytest.param.get('open_source_license'):
            assert p == 'BSD-3'
        else:
            assert p == 'MIT'

    def test_requirements(self):
        reqs_path = self.path / 'requirements.txt'
        assert reqs_path.exists()
        assert no_curlies(reqs_path)

    def test_dev_requirements(self):
        reqs_path = self.path / 'requirements-dev.txt'
        assert reqs_path.exists()
        assert no_curlies(reqs_path)

        with open(reqs_path) as f:
            contents = f.read()
        if pytest.param.get("strip_ipynb_output", "Y") == "Y":
            assert "nbstripout" in contents

    def test_makefile(self):
        makefile_path = self.path / 'Makefile'
        assert makefile_path.exists()
        assert no_curlies(makefile_path)

    def test_folders(self):
        library_name = pytest.param.get('library_name', 'core')
        expected_dirs = [
            'data',
            'data/external',
            'data/interim',
            'data/processed',
            'data/raw',
            'docs',
            'models',
            'notebooks',
            'references',
            'reports',
            'reports/figures',
            'src',
            f'src/{library_name}',
            f'src/{library_name}/data',
            f'src/{library_name}/features',
            f'src/{library_name}/models',
            f'src/{library_name}/visualization',
            'tests'
        ]

        ignored_dirs = [
            str(self.path)
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert set(abs_expected_dirs + ignored_dirs) == set(abs_dirs)
