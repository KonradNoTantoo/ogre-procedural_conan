from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(docker_32_images=True, pip_install=["mako"])
    builder.add_common_builds(shared_option_name="ogre-procedural:shared")
    builder.run()
