function [x, iteration] = Newtons_Method(f, df, x0, K, tol)
    % Set default values if not provided
    if nargin < 5
        tol = 1e-10;  % Default maximum number of iterations
    end

    if nargin < 4
        K = 100;  % Default tolerance
    end

    x = x0;  % Initial guess

    % Iterate up to maximum number of iterations
    for k = 1:K
        % Evaluate the function and its derivative at the current value of x
        fx = f(x);
        dfx = df(x);
        
        % Compute the next iteration using Newton's method formula
        x_new = x - fx / dfx;

        % Check for convergence
        if abs(fx) < tol
            iteration = k;  % Return the iteration count
            return
        end
        
        % Update x for the next iteration
        x = x_new;
    end
    
    iteration = K;  % Return the maximum iteration count
end
