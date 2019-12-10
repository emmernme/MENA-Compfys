#include <cmath>
#include <vector>
using namespace std;

#pragma once
class Planet {
	public:
		double dim; // 2D or 3D?

		// Planet properties
		double mass;
		double *position;
		double *velocity;
		double E_potential;
		double E_kinetic;

		// Methods to initialize Planet
		Planet(int dim, double mass, double* position, double* velocity);
		Planet(double mass, double x, double y, double z, double vx, double vy, double vz);
		Planet(double mass, double x, double y, double vx, double vy);

		// Various Planet-functions
		double planetary_distance(Planet secondPlanet);
		double gravitational_force(Planet secondPlanet, double G_const);
		double acceleration(Planet secondPlanet, double G_const);
		double kinetic_energy();
		double potential_energy(Planet secondPlanet, double G_const);
};