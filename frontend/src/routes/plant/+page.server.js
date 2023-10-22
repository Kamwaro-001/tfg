import { add_tree, get_trees } from '$lib/features/trees.js';

/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const response = await get_trees(),
		trees = response;
	return { trees };
}

export const actions = {
	default: async ({ request, locals }) => {
		/** @type {FormData} */
		const form = await request.formData();

		/** @type {object} */
		const data = {
			genus: form.get('genus'),
			more_info: form.get('more_info'),
			files: form.get('files') === '' ? null : form.get('files'),
			username: locals.profile.id
		};
		console.log(data);
		// /** @type {object} */
		const msg = await add_tree(data);
		console.log(msg);
	}
};
