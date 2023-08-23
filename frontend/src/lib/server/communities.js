import axios from 'axios';

export const getCommunities = async () => {
	const response = await axios.get('http://127.0.0.1:8000/api/communities');
	return response.data;
};
