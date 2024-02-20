import methods


# Tuples with the name of the arch that will be used in VS, mapped to our internal arch names.
# For Windows platforms, Win32 is what VS wants. For other platforms, it can be different.
def get_platforms():
    return [("x64", "x86_64")]


def get_configurations():
    return [
        ("editor", "Editor Debug", "Yes"), 
        ("editor", "Editor Release", "No"),
        ("template_debug", "Game Debug", "Yes"),
        ("template_release", "Game Release", "Yes"), 
        ("template_release", "Game Shipping", "No")
    ]


def get_build_prefix(env):
    batch_file = methods.find_visual_c_batch_file(env)
    return [
        "set &quot;plat=$(PlatformTarget)&quot;",
        "(if &quot;$(PlatformTarget)&quot;==&quot;x64&quot; (set &quot;plat=x86_amd64&quot;))",
        f"call &quot;{batch_file}&quot; !plat!",
    ]
