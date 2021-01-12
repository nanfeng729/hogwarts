import pytest
import yaml
import allure


class TestYaml:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_yaml(self, env):
        if 'test' in env:
            print(env)
            print(f"这是测试环境，ip是{env['test']}")

        if 'product' in env:
            print(f"这是生产环境,ip是{env['product']}")
