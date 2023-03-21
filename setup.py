from setuptools import setup, find_namespace_packages

setup(
    name="src\\test_version_powerhouse_helper",
    version="1",
    description="This is your console assistant by Python Powerhouse",
    author="Python Powerhouse",
    license="MIT",
    url="https://github.com/NovykovDaniil/python-core-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    data_files=[
        (
            "src\\test_version_powerhouse_helper\\GameGooseKiller\\font",
            ["src\\test_version_powerhouse_helper\\GameGooseKiller\\font\\UA Propisi.ttf"],
        ),
        (
            "src\\test_version_powerhouse_helper\\GameGooseKiller\\image",
            [
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\background.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\bonus.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\boom.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\enemy.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Farm-Goose.ico",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\gameover.png",
            ],
        ),
        (
            "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\background",
            [
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-1.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-2.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-3.png",
            ],
        ),
        (
            "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\Goose",
            [
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-1.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-2.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-3.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-4.png",
                "src\\test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-5.png",
            ],
        ),
    ],
    include_package_data=True,
    include_dirs=True,
    install_requires=["pygame", "prettytable", "prompt-toolkit"],
    entry_points={
        "console_scripts": ["powerhouse-helper=src\\test_version_powerhouse_helper.main:run"]
    },
)
