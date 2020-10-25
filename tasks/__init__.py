from invoke import Collection

from . import environment, git, integration

namespace = Collection()
namespace.add_collection(environment)
namespace.add_collection(git)
namespace.add_collection(integration)
