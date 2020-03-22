#include <cstdlib>
#include <OgreProcedural/ProceduralStableHeaders.h>
#include <OgreProcedural/Procedural.h>

int main()
{
	Ogre::Root root("", "");
	Ogre::RenderSystemList const & renderers = root.getAvailableRenderers(); 	

	if ( renderers.empty() ) return EXIT_SUCCESS;

	root.Ogre::Root::setRenderSystem(renderers[0]);

	Procedural::SphereGenerator()
		.setRadius(3.33)
		.setPosition(5.05, 6.06, 7.07)
		.realizeMesh();

	return EXIT_SUCCESS;
}
