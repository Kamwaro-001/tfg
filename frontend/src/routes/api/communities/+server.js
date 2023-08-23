import { getCommunities } from '$lib/server/communities';
import { json } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export async function GET() {
	try {
		const communities = await getCommunities();
		return json({ communities });
	} catch (/** @type {any} */ e) {
		return json({
			message: e.message
		});
	}
}
