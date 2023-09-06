import axios from 'axios';

export const getCommunities = async () => {
	const response = await axios.get('/api/communities');
	return response.data;
};

export const addCommunity = async (/** @type {any} */ community) => {
	try {
		return (
			await axios.post('/api/communities', { community }),
			{
				message: 'success'
			}
		);
	} catch (error) {
		return {
			message: error
		};
	}
};
