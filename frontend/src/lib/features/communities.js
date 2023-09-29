import axios from 'axios';

export const getCommunities = async () => {
	const response = await axios.get('/api/communities');
	return response.data;
};

export const add_community = async (/** @type {any} */ community) => {
	try {
		await axios.post('/api/communities/', community);

		return {
			message: 'success'
		};
	} catch (/** @type {any} */ error) {
		return {
			message: error.message
		};
	}
};
