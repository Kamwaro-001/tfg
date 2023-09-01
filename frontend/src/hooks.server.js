import { redirect } from '@sveltejs/kit';

// TODO set an axios base url

export const handle = async ({ event, resolve }) => {
	const sessionId = event.cookies.get('session_id');
	if (!sessionId) {
		throw redirect(303, '/');
	} else {
		event.locals.user = {
			logged_in: true,
			token: sessionId
		};
	}

	const query = event.url.searchParams.get('logout');
	if (Boolean(query) == true) {
		event.cookies.delete('session_id', { path: '/' });
	}

	return resolve(event);
};
