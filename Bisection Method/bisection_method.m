function [root, iteration] = bisection_method(f, a, b, tol, max_iter)
    
    % Check if the function has different signs at the endpoints
    if sign(f(a)) == sign(f(b))
        error('Function has the same sign at the endpoints of the interval.');
    end

    % Initialize iteration count
    iteration = 0;

    % Perform iterations
    while (b - a) / 2 > tol && iteration < max_iter
        c = (a + b) / 2;  % Compute midpoint

        % Check if c is the root
        if f(c) == 0
            root = c;
            return;
        end

        % Update interval
        if sign(f(c)) == sign(f(a))
            a = c;
        else
            b = c;
        end

        % Increment iteration count
        iteration = iteration + 1;
    end

    % Compute the final approximation of the root
    root = (a + b) / 2;
end
