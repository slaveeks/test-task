import dotenv from 'dotenv';
import path from 'path';

dotenv.config({path: path.join(__dirname, '..', '..', '.env')});

/**
 * Config class
 *
 * By default there are empty values because some values might be empty
 */
export class Config {
  /**
   * SERVER OPTIONS
   */
  public static SERVER_HOST: string = process.env.SERVER_HOST || 'http://localhost';
  public static SERVER_PORT: string = process.env.SERVER_PORT || '5000';
}
