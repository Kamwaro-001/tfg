import { getCommunities } from '$lib/features/communities';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
    const response = await getCommunities()
    const communities = response
    return { communities };
};