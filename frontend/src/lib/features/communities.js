import axios from 'axios';

export const getCommunities = async () => {
	const response = await axios.get('http://127.0.0.1:8000/api/communities');
	return response.data;
};

export const addCommunity = async (/** @type {any} */ community) => {
	try {
		return (
			await axios.post('http://127.0.0.1:8000/api/communities', { community }),
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
