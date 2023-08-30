import { getCommunities } from '$lib/server/communities';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	const communities = await getCommunities();

	const community = communities.find((/** @type {{ id: number; }} */ community) => community.id === parseInt(params.id));
	return {
		community
	};
}
