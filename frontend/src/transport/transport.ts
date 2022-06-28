import {SortedData} from './types/SortedData';
import {TotalSum} from './types/TotalSum';
import {Config} from '../config/config';

/**
 * Transport class
 *
 */
export class Transport {
  /**
   * Get sum of orders
   *
   * @return {Promise<TotalSum>} - response with sum of orders
   */
  public static async getSumOfOrders():
      Promise<TotalSum> {
    const response = await fetch(Config.SERVER_URL +
        + '/test-task/api/v1.0/sum', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }

  /**
   * Get all data
   *
   * @return {Promise<any>} - response with all data
   */
  public static async getAllData(): Promise<any> {
    const response = await fetch(Config.SERVER_URL +
        + '/test-task/api/v1.0/all_data', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }

  /**
   * Get ordered data
   *
   * @return {Promise<any>} - response with ordered data
   */
  public static async getOrderedData(): Promise<SortedData | undefined> {
    const response = await fetch(Config.SERVER_URL +
        + '/test-task/api/v1.0/ordered_data', {
      method: 'GET',
      headers: {
        accept: 'application/json',
      },
    });
    return await response.json();
  }
}

